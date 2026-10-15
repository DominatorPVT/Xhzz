<div align="center">

# ⚡ Action VPS — Temporary Linux Sessions

**Ubuntu runner or Arch Linux container for temporary development and debugging**

[![Stars](https://img.shields.io/github/stars/DominatorPVT/Xhzz?style=for-the-badge&color=yellow)](https://github.com/DominatorPVT/Xhzz/stargazers)
[![Forks](https://img.shields.io/github/forks/DominatorPVT/Xhzz?style=for-the-badge&color=blue)](https://github.com/DominatorPVT/Xhzz/forks)

</div>

> **Not a real VPS or a permanent hosting service.** Sessions use disposable CI environments. Check your provider's current acceptable-use rules, minutes allowance, billing settings, and job limits before running. Do not use CI runners for unrelated long-running hosting or to bypass usage limits.
>
> **Connection status:** The workflows attempt SSH through a Cloudflare Quick Tunnel. End-to-end SSH connectivity has not been verified for these configurations. A `trycloudflare.com` URL in the logs only confirms tunnel creation, not successful SSH access. Do not assume Quick Tunnels provide the same capabilities or access controls as a configured named tunnel with Cloudflare Access.

## Choose which Linux environment to run

The two GitHub workflows are **independent and manual-only**. Running Arch does not start Ubuntu, and running Ubuntu does not start Arch.

| Actions workflow | File | Environment | Login | Session duration |
|---|---|---|---|---|
| **🐧 Arch Linux Session** | `.github/workflows/arch-vps.yml` | `archlinux:base` container on an Ubuntu 24.04 runner | Fresh password printed in the run logs | Fixed 300-minute session after setup; job limit 350 minutes |
| **🖥️ Ubuntu Session** | `.github/workflows/ubuntu.yml` | GitHub's `ubuntu-latest` runner | Legacy fixed password | Keep-alive step: 300 minutes, plus setup time; job limit 350 minutes |

**Arch is container-based**, not an Arch VM or an Arch host kernel. It provides Arch userspace and `pacman`; it shares the Ubuntu runner's kernel. A full systemd boot, custom kernel, and privileged hardware access are not provided.

> **Password/log security warning:** Both environments print login credentials in CI logs. Anyone with access to those logs may be able to control the session; in a public repository the logs may be public. Use a private repository with restricted Actions/pipeline access, do not place sensitive data or CI secrets in these sessions, and cancel promptly when finished. A random password is not protection against log readers. Arch creates a fresh password per run, disables root SSH login, and grants the session user password-free sudo inside the container. The legacy Ubuntu jobs still use a fixed password and enable root SSH login; they are not a secure default.

## Quick start: choose an environment and run

### 1. Select Ubuntu or Arch

In GitHub Actions, select **🖥️ Ubuntu Session** or **🐧 Arch Linux Session**. They are separate workflows; only the one you choose runs.

### 2. Click Run workflow

Select the branch containing the workflow and click **Run workflow**. There is **no public-key input and no duration input**. You do not need to create an SSH key.

Open the run logs for the tunnel hostname, username (`vpsuser`), password, and SSH command. For Arch, the **Configure password SSH** step prints the host-key fingerprint, and the final step prints connection details with a fresh password generated for that run. Ubuntu's legacy connection details are in **Cloudflare Tunnel**. Arch displays an **ARCH LOGIN DETAILS** box; copy only the unprefixed, single-line command below **Termux CMD**, paste it into Termux, then enter the password from the same box when prompted.

There is no time selection: Arch uses a fixed five-hour session after setup, with a 350-minute overall job timeout. CI quotas or provider/runner limits can end a run earlier. Cancel the workflow to stop earlier.

### 3. Connect from your device

You need an OpenSSH client and `cloudflared` installed **on the client device**, not just the CI runner. This is not inherently Termux-only: compatible Linux/macOS clients can also use an SSH ProxyCommand. Windows clients may need different installation and quoting. Specific GUI clients have not been verified.

For Android Termux:

```bash
pkg update
pkg install openssh cloudflared
```

Copy the command printed in **your current run**. Its shape is:

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no \
  -o ProxyCommand='cloudflared access ssh --hostname YOUR-HOST.trycloudflare.com' \
  vpsuser@YOUR-HOST.trycloudflare.com
```

Replace both hostname placeholders. Enter the password printed in your current run when SSH prompts for it; nothing appears while you type. Do not reuse a password from an earlier Arch run. Compare the SSH host-key fingerprint with the one printed by your run before accepting it. Do not disable host-key checking.

**This Quick Tunnel SSH path is experimental.** If it does not connect, see troubleshooting below; successful YAML validation is not a live connectivity test.

### 4. Use Arch tools

Both Arch jobs (GitHub and GitLab) install all the explicitly configured Ubuntu tools: **OpenSSH, curl, wget, net-tools, sudo, Neofetch, tmux**, and **cloudflared**. On Arch, `openssh` includes the SSH server that Ubuntu packages as `openssh-server`. This matches the project's install list, not every additional tool bundled in a GitHub-hosted Ubuntu runner image. Neofetch displays system info automatically on interactive SSH login; run `neofetch` any time to see it again. The login banner is skipped for non-interactive commands and file transfers. Reported kernel/hardware information belongs to the shared CI host, not a dedicated Arch machine.

Neofetch is archived upstream. The workflow installs it from a pinned upstream commit and verifies its SHA-256 checksum rather than relying on an Arch package being available. No Fastfetch is installed by this workflow.

To install development tools **inside the Arch session**:

```bash
sudo pacman -Syu --needed git python nodejs npm
cat /etc/os-release
uname -r  # The kernel belongs to the underlying Ubuntu host.
tmux
neofetch
```

Arch is rolling-release. The workflow performs a full `pacman -Syu` upgrade before setup; the image and package versions are not pinned for reproducible builds.

### 5. End the session

The session stops automatically at its fixed session/job limit. To stop earlier, use **Cancel workflow** in GitHub Actions. Closing your SSH client does not stop the workflow or its consumption of CI minutes. Save your work before the run ends: nothing is backed up automatically.

## Ubuntu workflow (legacy password authentication)

1. Open **Actions → 🖥️ Ubuntu Session → Run workflow**.
2. Select the branch and start the run.
3. Open the **Cloudflare Tunnel** step for the connection command and legacy login details.

This workflow is preserved for compatibility, not recommended as a secure default. It uses a fixed password in source/logs and the same unverified Quick Tunnel SSH approach. `ubuntu-latest` and its available packages can change, so setup may need maintenance.

## GitLab CI: select Ubuntu or Arch

The root `.gitlab-ci.yml` includes `.gitlab/arch.yml`. Import **both files** (or the entire repository) into GitLab; do not use the Arch file alone as the CI entry point.

1. Open **Build / CI/CD → Pipelines → New pipeline / Run pipeline**.
2. Choose the branch containing these files.
3. Set **`LINUX_DISTRO`** to **`ubuntu`** or **`arch`** (default: `ubuntu`).
4. Click **Run pipeline** and open the selected **`ubuntu`** or **`arch`** job logs for the password and SSH command. No public key or duration variable is needed.

Only the selected job runs. Push and merge-request pipelines do not start a session. These jobs start when you submit a web pipeline; there is no second manual Play step. If your GitLab version does not show dropdowns, enter the same variable names and values manually.

| Job | Configuration | Image | Authentication | Requested timeout |
|---|---|---|---|---|
| `ubuntu` | `.gitlab-ci.yml` | `ubuntu:22.04` | Legacy fixed password (see warning above) | 5 hours 50 minutes |
| `arch` | `.gitlab/arch.yml` | `archlinux:base` | Fresh per-run password in logs; root SSH disabled | 5 hours 50 minutes |

Arch has the same tools, interactive Neofetch banner, automatic password generation, experimental tunnel, readiness timeout, and process monitoring as the GitHub Arch workflow. Use the SSH command and host-key fingerprint from the current run, as described in the GitHub connection instructions above.

Use an **amd64 Linux Docker/Kubernetes runner that supports the `image:` setting**, with permission to install packages as root inside the job container and outbound network access. A shell executor does not supply the requested container image. Project/runner timeouts and available CI minutes can stop jobs earlier than their requested timeout. Closing SSH does not stop the pipeline: cancel the job to stop it early.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Arch workflow is missing | Ensure the selected repository/branch contains `.github/workflows/arch-vps.yml`, Actions is enabled, and you have permission to dispatch it. GitHub requires a manually dispatched workflow to exist on the default branch before it is normally available for manual runs. |
| No tunnel URL | Arch waits up to 120 seconds for a hostname, then fails with tunnel logs. Check network/provider errors. |
| URL exists but SSH fails | A generated URL is not an SSH health check. Quick Tunnel transport may not support this connection reliably. Consider a properly configured named tunnel with an SSH ingress service and Cloudflare Access, or another approved remote-debugging transport; neither is set up here. |
| `cloudflared: command not found` on your device | Install cloudflared on the client and make sure it is in PATH. |
| Password login fails | Use username `vpsuser` and the password from the current run. Copy the printed SSH command, which explicitly selects password authentication for Arch. |
| Host-key warning | Every run creates new host keys. Verify the current fingerprint; do not blindly ignore a mismatch. |
| Session stops early | Check workflow logs, cancellation, job timeout, CI quota, or a tunnel/SSH process exiting. |
| Files disappear | CI filesystems are disposable. Copy needed files out before cancellation or timeout; there is no automatic persistence. |

## Resources, costs, and limitations

- CPU, RAM, disk space, job duration, and included CI minutes depend on provider, runner type, repository visibility, and account plan. No fixed hardware allocation or unlimited free usage is promised.
- Billing and storage limits change; check your current account settings instead of relying on hardcoded quota tables.
- Each Quick Tunnel run gets a new hostname. No Cloudflare token is configured for this experimental Quick Tunnel setup; a named tunnel/Access deployment requires separate configuration.
- The Arch workflow has no GitHub token permissions and does not check out repository files. Password login with credentials in logs is not a replacement for correctly configured tunnel access controls.
- Downloaded cloudflared releases are currently unpinned and not checksum-verified. Do not use this setup for sensitive workloads.
- Local static checks do not verify live GitHub/GitLab runs, client compatibility, or Cloudflare SSH transport.

## Project structure

```text
Xhzz/
├── .github/
│   └── workflows/
│       ├── ubuntu.yml    # Ubuntu session (legacy authentication)
│       └── arch-vps.yml  # Independent Arch container session
├── .gitlab/
│   └── arch.yml          # Arch GitLab job, included by the root config
├── .gitlab-ci.yml        # Distro selector and Ubuntu GitLab job
└── README.md
```

## License

No `LICENSE` file is currently included. The previous MIT badge was removed rather than implying that a license has been supplied. The project owner should choose and add a license before others rely on reuse permissions.

## Support

- **UPI:** `dpdangergameryt@oksbi`
- **Telegram:** [Mãrlbörõ Çlôve 🥀🚬](https://t.me/DOMINATOR_XYZ)
- **Creator:** [Dominator](https://github.com/DominatorStufs)
