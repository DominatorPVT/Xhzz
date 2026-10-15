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
| **🐧 Arch Linux Session** | `.github/workflows/arch-vps.yml` | `archlinux:base` container on an Ubuntu 24.04 runner | Your SSH public key | Choose 15, 30, 60, or 120 minutes, plus setup time; job limit 140 minutes |
| **🖥️ Ubuntu Session** | `.github/workflows/ubuntu.yml` | GitHub's `ubuntu-latest` runner | Legacy fixed password | Keep-alive step: 300 minutes, plus setup time; job limit 350 minutes |

**Arch is container-based**, not an Arch VM or an Arch host kernel. It provides Arch userspace and `pacman`; it shares the Ubuntu runner's kernel. A full systemd boot, custom kernel, and privileged hardware access are not provided.

> **Legacy security warning:** The existing Ubuntu configurations on GitHub and GitLab contain a fixed password, print it in logs, and enable root SSH login. They also grant the session user password-free sudo. Do not treat them as secure access configurations or use them with sensitive data. The new Arch workflow uses key-only SSH and disables root login; it still grants sudo **inside the disposable container**. Their legacy authentication has not been changed; only names and the preinstalled tool list were adjusted.

## Quick start: Arch Linux on GitHub

### 1. Prepare your SSH key

On your own device, use an existing SSH key or create one:

```bash
ssh-keygen -t ed25519
cat ~/.ssh/id_ed25519.pub
```

Keep your private key (`id_ed25519`) on your device. **Only the public key (`id_ed25519.pub`) belongs in the workflow input.** Never paste a private key into GitHub or logs.

### 2. Start only the Arch workflow

1. Fork this repository, or use your own copy with Actions enabled.
2. Open **Actions → 🐧 Arch Linux Session → Run workflow**.
3. Select the branch containing `arch-vps.yml`.
4. Paste one complete, single-line OpenSSH public key into `ssh_public_key`.
5. Choose `duration_minutes` and click **Run workflow**.
6. Open the job logs. The configuration step prints the SSH host-key fingerprint; the final step prints the tunnel hostname and SSH command.

No server login password is printed or required. If your private key has a passphrase, your local SSH client may ask for that passphrase.

### 3. Connect from your device

You need an OpenSSH client and `cloudflared` installed **on the client device**, not just the CI runner. This is not inherently Termux-only: compatible Linux/macOS clients can also use an SSH ProxyCommand. Windows clients may need different installation and quoting. Specific GUI clients have not been verified.

For Android Termux:

```bash
pkg update
pkg install openssh cloudflared
```

Copy the command printed in **your current run**. Its shape is:

```bash
ssh -i ~/.ssh/id_ed25519 \
  -o ProxyCommand='cloudflared access ssh --hostname YOUR-HOST.trycloudflare.com' \
  vpsuser@YOUR-HOST.trycloudflare.com
```

Replace both hostname placeholders; change `-i` if your private key has a different path. Compare the SSH host-key fingerprint with the one printed by your run before accepting it. Do not disable host-key checking.

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

The session stops when the chosen time elapses. To stop earlier, use **Cancel workflow** in GitHub Actions. Closing your SSH client does not stop the workflow or its consumption of CI minutes. Save your work before the run ends: nothing is backed up automatically.

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
4. For Arch, also set **`SSH_PUBLIC_KEY`** to one OpenSSH public key and **`DURATION_MINUTES`** to `15`, `30`, `60`, or `120` (default: `30`). Never supply a private key.
5. Run the pipeline and open the selected **`ubuntu`** or **`arch`** job logs.

Only the selected job runs. Push and merge-request pipelines do not start a session. These jobs start when you submit a web pipeline; there is no second manual Play step. If your GitLab version does not show dropdowns, enter the same variable names and values manually.

| Job | Configuration | Image | Authentication | Requested timeout |
|---|---|---|---|---|
| `ubuntu` | `.gitlab-ci.yml` | `ubuntu:22.04` | Legacy fixed password (see warning above) | 5 hours 50 minutes |
| `arch` | `.gitlab/arch.yml` | `archlinux:base` | SSH key only; root SSH disabled | 2 hours 20 minutes |

Arch has the same tools, interactive Neofetch banner, key validation, experimental tunnel, readiness timeout, and process monitoring as the GitHub Arch workflow. Use the SSH command and host-key fingerprint from the current run, as described in the GitHub connection instructions above.

Use an **amd64 Linux Docker/Kubernetes runner that supports the `image:` setting**, with permission to install packages as root inside the job container and outbound network access. A shell executor does not supply the requested container image. Project/runner timeouts and available CI minutes can stop jobs earlier than their requested timeout. Closing SSH does not stop the pipeline: cancel the job to stop it early.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Arch workflow is missing | Ensure the selected repository/branch contains `.github/workflows/arch-vps.yml`, Actions is enabled, and you have permission to dispatch it. GitHub requires a manually dispatched workflow to exist on the default branch before it is normally available for manual runs. |
| Key validation fails | Paste one OpenSSH public key, not a private key or multiple keys. |
| No tunnel URL | Arch waits up to 120 seconds for a hostname, then fails with tunnel logs. Check network/provider errors. |
| URL exists but SSH fails | A generated URL is not an SSH health check. Quick Tunnel transport may not support this connection reliably. Consider a properly configured named tunnel with an SSH ingress service and Cloudflare Access, or another approved remote-debugging transport; neither is set up here. |
| `cloudflared: command not found` on your device | Install cloudflared on the client and make sure it is in PATH. |
| `Permission denied (publickey)` | Use the private key matching the workflow's public key and username `vpsuser`. |
| Host-key warning | Every run creates new host keys. Verify the current fingerprint; do not blindly ignore a mismatch. |
| Session stops early | Check workflow logs, cancellation, job timeout, CI quota, or a tunnel/SSH process exiting. |
| Files disappear | CI filesystems are disposable. Copy needed files out before cancellation or timeout; there is no automatic persistence. |

## Resources, costs, and limitations

- CPU, RAM, disk space, job duration, and included CI minutes depend on provider, runner type, repository visibility, and account plan. No fixed hardware allocation or unlimited free usage is promised.
- Billing and storage limits change; check your current account settings instead of relying on hardcoded quota tables.
- Each Quick Tunnel run gets a new hostname. No Cloudflare token is configured for this experimental Quick Tunnel setup; a named tunnel/Access deployment requires separate configuration.
- The Arch workflow has no GitHub token permissions and does not check out repository files. Key-only SSH is not a replacement for correctly configured tunnel access controls.
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
├── tests/               # Static CI configuration checks
└── README.md
```

## Validate configuration locally

```bash
python -m pip install -r tests/requirements.txt
python -m unittest discover -s tests -v
```

These checks parse YAML, validate Bash syntax, check tool parity and GitLab selection rules, and ensure both Arch job scripts stay in sync. They do not start a remote session or contact Cloudflare.

## License

No `LICENSE` file is currently included. The previous MIT badge was removed rather than implying that a license has been supplied. The project owner should choose and add a license before others rely on reuse permissions.

## Support

- **UPI:** `dpdangergameryt@oksbi`
- **Telegram:** [Mãrlbörõ Çlôve 🥀🚬](https://t.me/DOMINATOR_XYZ)
- **Creator:** [Dominator](https://github.com/DominatorStufs)
