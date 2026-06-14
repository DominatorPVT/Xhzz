<div align="center">

# ⚡ Action VPS

**Free temporary Ubuntu VPS via GitHub Actions & GitLab CI**

[![Stars](https://img.shields.io/github/stars/DominatorStufs/action-vps?style=for-the-badge&color=yellow)](https://github.com/DominatorStufs)
[![Forks](https://img.shields.io/github/forks/DominatorStufs/action-vps?style=for-the-badge&color=blue)](https://github.com/DominatorStufs)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Action VPS** gives you a free temporary Ubuntu shell via **Cloudflare Tunnel** — works 100% on GitHub Actions & GitLab CI. No token or signup required!

> ⚠️ Not a real VPS. Runs ~6 hours per session. All data is lost after session ends.

---

## ✅ Why Cloudflare Tunnel?

| Feature | Details |
|---|---|
| 💰 Cost | 100% Free |
| 🔑 Token needed | ❌ None |
| 🌐 Access | SSH via cloudflared |
| ⚡ Works on GitHub Actions | ✅ Yes |
| 🔒 Secure | Encrypted by Cloudflare |

---

## 🚀 Quick Start

### GitHub Actions

```
1. Star ⭐ & Fork 🍴 this repo
2. Go to Actions tab
3. Select "Action VPS" workflow
4. Click "Run workflow" ▶️
5. Open logs → find SSH details
```

### GitLab CI

```
1. Fork/import this repo on GitLab
2. Go to CI/CD → Pipelines
3. Click "Run pipeline"
4. Open job logs → find SSH details
```

---

## 🔌 How to Connect

First install cloudflared on your device:
```bash
# Download cloudflared
https://github.com/cloudflare/cloudflared/releases/latest
```

You will see this in the logs:

```
╔════════════════════════════════════════════╗
║           🚀 VPS LOGIN DETAILS             ║
╠════════════════════════════════════════════╣
║ 🌐 URL      : https://xxxx.trycloudflare.com
║ 👤 Username : vpsuser
║ 🔑 Password : Vps@2024#Secure
╠════════════════════════════════════════════╣
║ 💻 SSH CMD:
║ ssh -o ProxyCommand='cloudflared access ssh
║ --hostname URL' vpsuser@URL
╚════════════════════════════════════════════╝
```

**Connect via terminal:**
```bash
ssh -o ProxyCommand='cloudflared access ssh --hostname https://xxxx.trycloudflare.com' vpsuser@xxxx.trycloudflare.com
```

---

## 📦 Features

| Feature | Details |
|---|---|
| 🐧 OS | Ubuntu (latest) |
| 🌐 Tunnel | Cloudflare (100% free) |
| 🖥️ CPU | 2 cores |
| 💾 RAM | ~7 GB |
| 💿 Disk | ~30 GB |
| ⏳ Duration | ~6 hours |
| 🔄 New session | New URL every run |

---

## 💾 Storage Limits

### GitHub Free

| Type | Limit |
|---|---|
| Repository storage | Unlimited *(keep < 1 GB)* |
| Actions storage | 500 MB |
| Monthly reset | ❌ None |

### GitLab Free

| Type | Limit |
|---|---|
| Repository storage | 5 GB |
| CI/CD artifacts | 1 GB |
| Pipeline minutes | 400 min/month |

---

## 📂 Project Structure

```
action-vps/
├── .github/
│   └── workflows/
│       └── vps.yml
├── .gitlab-ci.yml
└── README.md
```

---

## ⚠️ Important Notes

- Session lasts **~6 hours** only
- **New URL every run**
- Manual start required every time
- All data is lost after session ends
- Install `cloudflared` on your local machine to connect

---

## 💖 Support

<div align="center">

**UPI** → `dpdangergameryt@oksbi`

**Telegram** → [@DOMINATOR_XYZ](https://t.me/DOMINATOR_XYZ)

**GitHub** → [DominatorStufs](https://github.com/DominatorStufs)

</div>

---

<div align="center">

Made with ❤️ by **[Dominator](https://github.com/DominatorStufs)**

*If you find this useful — drop a ⭐ it means a lot!*

</div>
