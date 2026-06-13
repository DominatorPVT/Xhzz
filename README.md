<div align="center">

# ⚡ Action VPS

**Free temporary Ubuntu VPS via GitHub Actions**

[![Stars](https://img.shields.io/github/stars/DominatorStufs/action-vps?style=for-the-badge&color=yellow)](https://github.com/DominatorStufs)
[![Forks](https://img.shields.io/github/forks/DominatorStufs/action-vps?style=for-the-badge&color=blue)](https://github.com/DominatorStufs)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Action VPS** gives you a temporary Ubuntu environment running inside GitHub Actions — with SSH access, a public tunnel URL, and `neofetch` pre-installed.

> ⚠️ This is **not** a real VPS. It runs for ~6 hours per session and resets every time.

---

## 🚀 Quick Start

```bash
1. Star ⭐ this repository
2. Fork 🍴 this repository
3. Open your forked repo → Actions tab
4. Select "Action VPS" workflow
5. Click "Run workflow" ▶️
6. Check logs for SSH credentials & tunnel URL
```

---

## 📦 Features

| Feature | Details |
|---|---|
| 🐧 OS | Ubuntu (latest) |
| 🔐 SSH | Random username & password (from logs) |
| 🌐 Tunnel | Random public URL (changes every run) |
| ⚡ Pre-installed | `neofetch` (auto-runs on start) |
| ⏳ Duration | ~6 hours per session |
| 🖐️ Start | Manual trigger only |

---

## 💾 Storage Limits

### GitHub Free

| Type | Limit |
|---|---|
| Repository storage | Unlimited *(keep < 1 GB)* |
| Actions storage | 500 MB |

### GitLab Free

| Type | Limit |
|---|---|
| Repository storage | 5 GB per namespace |
| CI/CD Job artifacts | 1 GB |
| Pipeline minutes | 400 min/month |

---

## 🔌 How to Connect via SSH

Use any SSH client (e.g. **Terminus**, **JuiceSSH**, **PuTTY**).

```
Host     → (from Actions logs)
Port     → 22
Username → (from Actions logs)
Password → (from Actions logs)
```

> 💡 Tip: Run `neofetch` after connecting to verify your environment.

---

## 📂 Project Structure

```
action-vps/
├── .github/
│   └── workflows/
│       └── vps.yml
└── README.md
```

---

## ⚠️ Important Notes

- Session lasts **~6 hours** only
- **URL & credentials change** on every run
- Workflow must be **started manually** each time
- All data is **lost** after session ends

---

## 💖 Support

If this project helped you, consider supporting:

<div align="center">

**UPI** → `dpdangergameryt@oksbi`

**Telegram** → [@DOMINATOR_XYZ](https://t.me/DOMINATOR_XYZ)

**GitHub** → [DominatorStufs](https://github.com/DominatorStufs)

</div>

---

<div align="center">

Made with 🚬 by **[Dominator](https://github.com/DominatorStufs)**

*If you find this useful — drop a ⭐ it means a lot!*

</div>
