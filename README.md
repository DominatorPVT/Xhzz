<div align="center">

# ⚡ Action VPS

**Free temporary Ubuntu VPS via GitHub Actions & GitLab CI**

[![Stars](https://img.shields.io/github/stars/DominatorStufs/action-vps?style=for-the-badge&color=yellow)](https://github.com/DominatorStufs)
[![Forks](https://img.shields.io/github/forks/DominatorStufs/action-vps?style=for-the-badge&color=blue)](https://github.com/DominatorStufs)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Action VPS** gives you a free temporary Ubuntu shell via **zrok** — works 100% on GitHub Actions & GitLab CI. Free account on [zrok.io](https://zrok.io) required!

> ⚠️ Not a real VPS. Runs ~6 hours per session. All data is lost after session ends.

---

## ✅ Why zrok?

| Feature | Details |
|---|---|
| 💰 Cost | 100% Free |
| 🔑 Token needed | ✅ Free signup on zrok.io |
| 🌐 Access | SSH tunnel |
| ⚡ Works on GitHub Actions | ✅ Yes |
| 🔒 Secure | Encrypted tunnel |

---

## 🚀 Quick Start

### GitHub Actions

```
1. Star ⭐ & Fork 🍴 this repo
2. Add ZROK_TOKEN in repo Secrets
3. Go to Actions tab
4. Select "Action VPS" workflow
5. Click "Run workflow" ▶️
6. Open logs → find SSH details
```

### GitLab CI

```
1. Fork/import this repo on GitLab
2. Add ZROK_TOKEN in CI/CD Variables
3. Go to CI/CD → Pipelines
4. Click "Run pipeline"
5. Open job logs → find SSH details
```

---

## 🔑 zrok Setup

```
1. Create a free account at zrok.io
2. Go to Dashboard → copy your Auth Token
3. GitHub: Settings → Secrets → New secret → ZROK_TOKEN
4. GitLab: Settings → CI/CD → Variables → ZROK_TOKEN
```

---

## 🔌 How to Connect

You will see this in the logs:

```
╔════════════════════════════════════════════╗
║           🚀 VPS LOGIN DETAILS             ║
╠════════════════════════════════════════════╣
║ 🌐 Address  : abc123.share.zrok.io:PORT
║ 👤 User     : vpsuser
║ 🔑 Pass     : Vps@2024#Secure
╠════════════════════════════════════════════╣
║ 💻 SSH CMD  : ssh -p PORT vpsuser@HOST
╚════════════════════════════════════════════╝
```

**Connect via terminal:**
```bash
ssh -p PORT vpsuser@abc123.share.zrok.io
```

---

## 📦 Features

| Feature | Details |
|---|---|
| 🐧 OS | Ubuntu (latest) |
| 🌐 Tunnel | zrok.io (100% free) |
| 🖥️ CPU | 2 cores |
| 💾 RAM | ~7 GB |
| 💿 Disk | ~30 GB |
| ⏳ Duration | ~6 hours |
| 🔄 New session | New details every run |

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
- **New SSH details every run**
- Manual start required every time
- All data is lost after session ends

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
