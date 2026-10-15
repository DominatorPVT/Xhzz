"""Static checks only: no package installation, SSH server, or tunnel is started."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class UniqueLoader(yaml.BaseLoader):
    """Keep YAML keys such as `on` as strings and reject duplicate keys."""


def construct_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
)


def load(path):
    return yaml.load((ROOT / path).read_text(), Loader=UniqueLoader)


def bash_check(script):
    subprocess.run(["bash", "-n"], input=script, text=True, check=True)


class CIConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.ubuntu = load(".github/workflows/ubuntu.yml")
        self.arch = load(".github/workflows/arch-vps.yml")
        self.gitlab = load(".gitlab-ci.yml")
        self.gitlab_arch = load(".gitlab/arch.yml")["arch"]
        self.arch_steps = self.arch["jobs"]["arch"]["steps"]

    def test_all_yaml_and_shell_syntax(self):
        for config in (self.ubuntu, self.arch):
            self.assertEqual(set(config["on"]), {"workflow_dispatch"})
            for job in config["jobs"].values():
                for step in job["steps"]:
                    if "run" in step:
                        bash_check(step["run"])
        for job in (self.gitlab["ubuntu"], self.gitlab_arch):
            self.assertTrue(all(isinstance(s, str) for s in job["script"]))
            bash_check("\n".join(job["script"]))
        # Check the inner Bash body as well as the outer heredoc wrapper.
        bash_check(self.gitlab_arch["script"][0].split("\n", 1)[1].rsplit("ARCH_SESSION", 1)[0])

    def test_ubuntu_rename(self):
        self.assertEqual(set(self.ubuntu["jobs"]), {"ubuntu"})
        self.assertEqual(self.ubuntu["name"], "🖥️ Ubuntu Session")
        self.assertFalse((ROOT / ".github/workflows/vps.yml").exists())
        self.assertNotIn("free-vps", self.gitlab)

    def test_gitlab_local_include_and_exclusive_web_selection(self):
        self.assertEqual(self.gitlab["include"], [{"local": "/.gitlab/arch.yml"}])
        variables = self.gitlab["variables"]
        self.assertEqual(variables["LINUX_DISTRO"]["value"], "ubuntu")
        self.assertEqual(variables["LINUX_DISTRO"]["options"], ["ubuntu", "arch"])
        for distro, job in (("ubuntu", self.gitlab["ubuntu"]), ("arch", self.gitlab_arch)):
            self.assertIn(job["stage"], self.gitlab["stages"])
            self.assertEqual(job["rules"], [
                {"if": f'$CI_PIPELINE_SOURCE == "web" && $LINUX_DISTRO == "{distro}"'}
            ])
            self.assertNotIn("only", job)
            self.assertNotIn("when", job)

    def test_arch_scripts_stay_in_sync(self):
        expected = "\n\n".join(
            "# " + step["name"] + "\n" + step["run"].rstrip()
            for step in self.arch_steps
        ) + "\n"
        self.assertEqual(
            self.gitlab_arch["script"],
            ["bash <<'ARCH_SESSION'\n" + expected + "ARCH_SESSION\n"],
        )
        self.assertNotIn("${{", self.gitlab_arch["script"][0])

    def test_preinstalled_tool_parity(self):
        arch_install = self.arch_steps[0]["run"]
        for package in ("openssh", "curl", "wget", "net-tools", "sudo", "tmux"):
            self.assertIn(package, arch_install.split("pacman -Syu", 1)[1].splitlines()[0].split())
        for config in (self.ubuntu["jobs"]["ubuntu"]["steps"][0]["run"], "\n".join(self.gitlab["ubuntu"]["script"])):
            for tool in ("openssh-server", "curl", "wget", "net-tools", "neofetch", "tmux"):
                self.assertIn(tool, config)
        self.assertIn("install -m 755 /tmp/neofetch /usr/local/bin/neofetch", arch_install)
        self.assertIn("sha256sum --check", arch_install)
        self.assertNotIn("fastfetch", "\n".join(s["run"] for s in self.arch_steps).lower())

    def test_arch_duration_and_security_settings(self):
        choices = self.arch["on"]["workflow_dispatch"]["inputs"]["duration_minutes"]
        self.assertEqual(choices["options"], ["15", "30", "60", "120"])
        self.assertEqual(self.gitlab["variables"]["DURATION_MINUTES"]["options"], choices["options"])
        self.assertEqual(self.gitlab["variables"]["DURATION_MINUTES"]["value"], choices["default"])
        self.assertEqual(self.gitlab_arch["image"], self.arch["jobs"]["arch"]["container"]["image"])
        script = self.arch_steps[1]["run"]
        for option in ("PermitRootLogin no", "PasswordAuthentication no", "AuthenticationMethods publickey"):
            self.assertIn(option, script)

    @unittest.skipUnless(shutil.which("ssh-keygen"), "requires local OpenSSH client")
    def test_public_key_validation(self):
        script = self.arch_steps[1]["run"]
        validation = script[script.index('case "$SSH_PUBLIC_KEY"'):script.index("install -m 600")]
        with tempfile.TemporaryDirectory() as tmp:
            key = Path(tmp) / "key"
            subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", str(key)], check=True)
            public = key.with_suffix(".pub").read_text()
            validation = validation.replace("/tmp/public-key", str(Path(tmp) / "public-key"))
            for value, valid in ((public.strip(), True), (key.read_text(), False), (public * 2, False), ("ssh-ed25519 invalid", False), ("", False)):
                with self.subTest(valid=valid, prefix=value[:20]):
                    result = subprocess.run(
                        ["bash", "-euo", "pipefail", "-c", validation],
                        env={**os.environ, "SSH_PUBLIC_KEY": value},
                        capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode == 0, valid)

    def test_banner_does_not_pollute_noninteractive_commands(self):
        step = next(s for s in self.arch_steps if s["name"] == "Configure Neofetch login banner")
        banner = step["run"].split("<<'PROFILE'\n", 1)[1].split("\nPROFILE", 1)[0]
        bash_check(banner)
        result = subprocess.run(["bash", "-c", banner], capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
