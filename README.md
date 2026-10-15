<div align="center">

# ⚡ Action VPS — Temporary Linux Sessions

**Ubuntu runner or Arch Linux container for temporary development and debugging**

[![Stars](https://img.shields.io/github/stars/DominatorPVT/Xhzz?style=for-the-badge&color=yellow)](https://github.com/DominatorPVT/Xhzz/stargazers)
[![Forks](https://img.shields.io/github/forks/DominatorPVT/Xhzz?style=for-the-badge&color=blue)](https://github.com/DominatorPVT/Xhzz/forks)

</div>

> **Not a real VPS or a permanent hosting service.** Sessions use disposable CI environments. Check your provider's current acceptable-use rules, minutes allowance, billing settings, and job limits before running. Do not use CI runners for unrelated long-running hosting or to bypass usage limits.
>
> **Connection status:** User-provided Termux logs show a successful Arch SSH password login and interactive Neofetch output. Earlier attempts also showed DNS errors and a broken pipe, so this is not a reliability guarantee or verification of every GitHub/GitLab configuration. A `trycloudflare.com` URL in the logs only confirms tunnel creation, not successful SSH access. Do not assume Quick Tunnels provide the same capabilities or access controls as a configured named tunnel with Cloudflare Access.

## Requirements

### On your device

| Requirement | Purpose |
|---|---|
| Termux on Android, or another terminal with a compatible SSH client | Run the connection command. Android root access is not required. |
| **OpenSSH client** (`ssh`) | Connect to the remote Linux session. |
| **cloudflared on the client device** | Run the SSH ProxyCommand. Installing it only in the CI runner is not enough. |
| Working internet and DNS | Resolve and reach the current run's `trycloudflare.com` hostname. Network restrictions or an interrupted connection can break access. |
| Access to the current workflow/pipeline logs | Copy the current hostname, login details, and command. Each new run can use a different hostname. |

**Termux: install the required client packages once**

```bash
pkg update
pkg install openssh cloudflared
```

**Check that both commands are available before connecting:**

```bash
command -v ssh
command -v cloudflared
ssh -V
cloudflared --version
```

Both `command -v` checks should print a path, and the version commands should print their versions. If either command is missing, fix that installation before retrying SSH. `pkg` is a Termux command; desktop users should install OpenSSH and cloudflared using their platform's installation instructions.

**Not required for this password-login setup:** an SSH key, `sshpass`, Android root, a local Arch installation, or Python/Node.js on your phone. Neofetch and tmux are installed in the remote session, not by the Termux client setup above. No Cloudflare account/token is configured for the experimental Quick Tunnel flow; a named tunnel/Access setup has different requirements.

### On GitHub or GitLab

| Platform | Requirements |
|---|---|
| GitHub Actions | A repository containing these workflow files, Actions enabled, permission to run the manual workflow and read its logs, and sufficient runner availability/CI allowance. A new workflow normally needs to exist on the default branch to be available for manual dispatch. |
| GitLab CI | The root `.gitlab-ci.yml` **and** included `.gitlab/arch.yml`, permission to run web pipelines/read logs, available CI allowance, and an **amd64 Linux container runner** that supports `image:`. See [GitLab instructions](#gitlab-ci-select-ubuntu-or-arch). |
| Job environment | Outbound access for distro package repositories, Neofetch/cloudflared downloads, and Cloudflare tunnel service connections. Arch jobs need root within their disposable container for package and SSH setup. |

Prefer a private repository with restricted log access: the login credentials are public in this project's source and are printed in job logs. Never provide sensitive CI secrets or personal data to these sessions. Provider acceptable-use rules, quotas, and runner/job timeout settings still apply.

## Latest connection updates

- Ubuntu and Arch still start manually, without SSH-key or duration inputs.
- Login commands now use `LogLevel=ERROR` to avoid routine debug chatter and retain SSH errors.
- Client keep-alives run every 30 idle seconds with a limit of three unanswered checks. They do not fix a dead tunnel, DNS failure, or expired CI session.
- Password entry remains manual; it is shown separately in the login box. Copy only the command after the decorative `║`, not the box border or Markdown links.
- `send packet: type 98` is an SSH debug message, not a command or an Arch error. Use `neofetch`, not `neofetxh`.

## Choose which Linux environment to run

The two GitHub workflows are **independent and manual-only**. Running Arch does not start Ubuntu, and running Ubuntu does not start Arch.

| Actions workflow | File | Environment | Login | Session duration |
|---|---|---|---|---|
| **🐧 Arch Linux Session** | `.github/workflows/arch-vps.yml` | `archlinux:base` container on an `ubuntu-latest` runner | Same fixed password as Ubuntu, printed in the logs | Fixed 300-minute session after setup; job limit 350 minutes |
| **🖥️ Ubuntu Session** | `.github/workflows/ubuntu.yml` | GitHub's `ubuntu-latest` runner | Legacy fixed password | Keep-alive step: 300 minutes, plus setup time; job limit 350 minutes |

**Arch is container-based**, not an Arch VM or an Arch host kernel. It provides Arch userspace and `pacman`; it shares the Ubuntu runner's kernel. A full systemd boot, custom kernel, and privileged hardware access are not provided.

> **Password/log security warning:** Both environments print login credentials in CI logs. Anyone with access to those logs may be able to control the session; in a public repository the logs may be public. Use a private repository with restricted Actions/pipeline access, do not place sensitive data or CI secrets in these sessions, and cancel promptly when finished. Both environments now use the same fixed login (`vpsuser` / `vps@2026xyz`), which is public in the source and logs. Arch disables root SSH login and grants the session user password-free sudo inside the container. The legacy Ubuntu jobs still use a fixed password and enable root SSH login; they are not a secure default.

## Quick start: choose an environment and run

### 1. Select Ubuntu or Arch

In GitHub Actions, select **🖥️ Ubuntu Session** or **🐧 Arch Linux Session**. They are separate workflows; only the one you choose runs.

### 2. Click Run workflow

Select the branch containing the workflow and click **Run workflow**. There is **no public-key input and no duration input**. You do not need to create an SSH key.

Open the run logs for the tunnel hostname, username (`vpsuser`), password, and SSH command. For Arch, **🔐 Configure SSH** prints the host-key fingerprint and **🌐 Cloudflare Tunnel** prints the login details, using the same fixed password as Ubuntu. Ubuntu's legacy connection details are in **Cloudflare Tunnel**. Arch displays an **ARCH LOGIN DETAILS** box in the same format as Ubuntu. Copy the command after the decorative `║` on the **Termux CMD** line, paste it into Termux, then enter the password from the box when SSH prompts.

There is no time selection: Arch uses a fixed five-hour session after setup, with a 350-minute overall job timeout. CI quotas or provider/runner limits can end a run earlier. Cancel the workflow to stop earlier.

### 3. Connect from your device

You need an OpenSSH client and `cloudflared` installed **on the client device**, not just the CI runner. This is not inherently Termux-only: compatible Linux/macOS clients can also use an SSH ProxyCommand. Windows clients may need different installation and quoting. Specific GUI clients have not been verified.

Complete the [client requirements](#on-your-device) first. For Ubuntu or Arch, copy the command printed in **your current run**. Its shape is:

```bash
ssh -o LogLevel=ERROR -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ProxyCommand='cloudflared access ssh --hostname YOUR-HOST.trycloudflare.com' vpsuser@YOUR-HOST.trycloudflare.com
```

Replace both hostname placeholders. Enter `vps@2026xyz` when SSH asks for the password; nothing appears while you type. Compare the host-key fingerprint with the Configure SSH logs before accepting a new host key. Do not disable host-key checking. The command is plain SSH, as in Ubuntu: `sshpass` is not needed and the password is displayed separately rather than embedded in the command.

**This Quick Tunnel SSH path is experimental.** If it does not connect, see troubleshooting below; successful YAML validation is not a live connectivity test.

### Normal terminal output and disconnects

The printed command uses `LogLevel=ERROR` to suppress SSH diagnostic chatter while retaining errors. Do not add `-v`, `-vv`, or `-vvv` for everyday use. Those flags deliberately print protocol details mixed with your shell output. For a diagnostic session, remove `-o LogLevel=ERROR` and use `-vvv` only while collecting logs.

- `Authenticated ... using "password"` followed by `[vpsuser@... ~]$` means login succeeded.
- `send packet: type 98`, `window-change`, and `obfuscate_keystroke_timing` are debug messages, not commands or server failures. Never copy their numbers into the shell.
- Run `neofetch`, not `neofetxh`. To redraw a cluttered terminal, use `clear` or Ctrl+L.
- If already connected with `-vvv`, type `exit`, then reconnect with the current run's normal command (without the decorative `║`). If typing is difficult because logs keep appearing, press Enter and then type `~.` at the beginning of a fresh line to disconnect.
- The command requests an SSH server response every 30 idle seconds and disconnects after three unanswered keep-alives. This can help detect a dead connection and may prevent some idle timeouts, but it cannot repair DNS failures, an expired hostname, a stopped CI job, or a failed Cloudflare tunnel.
- A `Broken pipe` before authentication does not, by itself, identify a wrong password or a server bug. If it recurs, save the client diagnostics and the corresponding server/tunnel logs before restarting the run. A later successful login does not establish the cause of the earlier disconnect.

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
| `arch` | `.gitlab/arch.yml` | `archlinux:base` | Same fixed password as Ubuntu; root SSH disabled | 5 hours 50 minutes |

Arch uses the same five-step sequence as Ubuntu: **System Setup → Create User → Configure SSH → Cloudflare Tunnel → Keep Alive**. Both Arch CI configurations retain the installed tools, interactive Neofetch banner, experimental tunnel with the same initial ten-second wait as Ubuntu and an explicit missing-URL check, and a fixed five-hour keep-alive. Ongoing process monitoring is not included in this simplified layout. Use the SSH command and host-key fingerprint from the current run, as described in the GitHub connection instructions above.

Use an **amd64 Linux Docker/Kubernetes runner that supports the `image:` setting**, with permission to install packages as root inside the job container and outbound network access. A shell executor does not supply the requested container image. Project/runner timeouts and available CI minutes can stop jobs earlier than their requested timeout. Closing SSH does not stop the pipeline: cancel the job to stop it early.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Arch workflow is missing | Ensure the selected repository/branch contains `.github/workflows/arch-vps.yml`, Actions is enabled, and you have permission to dispatch it. GitHub requires a manually dispatched workflow to exist on the default branch before it is normally available for manual runs. |
| No tunnel URL | Arch waits ten seconds for a hostname, then fails with tunnel logs if none was found. Slow tunnel startup may require retrying the workflow. Check network/provider errors. |
| URL exists but SSH fails | A generated URL is not an SSH health check. Quick Tunnel transport may not support this connection reliably. Consider a properly configured named tunnel with an SSH ingress service and Cloudflare Access, or another approved remote-debugging transport; neither is set up here. |
| `cloudflared: command not found` on your device | Install cloudflared on the client and make sure it is in PATH. |
| `no such host` / DNS lookup failure | Use the latest run's hostname without Markdown brackets or links. Confirm the workflow is still active and check the device's DNS/network. This error occurs before password authentication. |
| `Broken pipe` / `UNKNOWN port 65535` | Inspect the client, tunnel, and SSH server logs for the same attempt. With a ProxyCommand, port 65535 in this error is not an instruction to open that port. A later successful login does not prove the cause of an earlier disconnect. |
| Debug output such as `type 98` floods the shell | Reconnect without `-v`, `-vv`, or `-vvv` using the normal command. Do not type debug packet numbers into the remote shell. |
| Password login fails | Use username `vpsuser` and the password from the current run. Copy the SSH command after the decorative `║` prefix; use the password shown separately in the box. |
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
