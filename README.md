<div align="center">

# ⚡ Action VPS

**Free temporary Ubuntu VPS via GitHub Actions & GitLab CI**

[![Stars](https://img.shields.io/github/stars/DominatorStufs/action-vps?style=for-the-badge&color=yellow)](https://github.com/DominatorStufs)
[![Forks](https://img.shields.io/github/forks/DominatorStufs/action-vps?style=for-the-badge&color=blue)](https://github.com/DominatorStufs)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Action VPS** gives you a temporary Ubuntu environment running inside GitHub Actions or GitLab CI — with SSH access via **serveo.net** tunnel.

> ⚠️ This is **not** a real VPS. It runs for ~6 hours per session and resets every time.

---

## ✅ Why serveo.net?

| Feature | Details |
|---|---|
| 💰 Cost | 100% Free |
| 🔑 Token needed | ❌ No token, no signup |
| 🌐 Tunnel type | SSH reverse tunnel |
| ⚡ Setup | Zero config needed |
| 🔒 Secure | Encrypted SSH tunnel |

---

## 🚀 Quick Start

### GitHub Actions

```
1. Star ⭐ & Fork 🍴 this repository
2. Go to Actions tab
3. Select "Action VPS" workflow
4. Click "Run workflow" ▶️
5. Open the running job logs
6. Find HOST, PORT, USERNAME, PASSWORD in logs
```

### GitLab CI

```
1. Import/fork this repo on GitLab
2. Go to CI/CD → Pipelines
3. Click "Run pipeline"
4. Open job logs
5. Find HOST, PORT, USERNAME, PASSWORD in logs
```

> ✅ No secrets or tokens needed — just fork and run!

---

## 🔌 How to Connect via SSH

Use any SSH client (**Terminus**, **JuiceSSH**, **PuTTY**, **Termux**).

```
Host     → serveo.net
Port     → (PORT from logs)
Username → (USERNAME from logs)
Password → (PASSWORD from logs)
```

### Termux / Terminal one-line command:

```bash
ssh USERNAME@serveo.net -p PORT
```

Example:
```bash
ssh abc123@serveo.net -p 45231
```

---

## 📦 Features

| Feature | Details |
|---|---|
| 🐧 OS | Ubuntu (latest) |
| 🔐 SSH | Random username & password (auto generated) |
| 🌐 Tunnel | serveo.net (no token needed!) |
| 🔄 Auto reconnect | autossh keeps tunnel alive |
| ⏳ Duration | ~6 hours per session |
| 🖐️ Start | Manual trigger only |

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
| Repository storage | 5 GB per namespace |
| CI/CD Job artifacts | 1 GB |
| Pipeline minutes | 400 min/month |
| Monthly reset | ✅ Pipeline minutes reset monthly |

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
- **HOST is always `serveo.net`** — only PORT changes each run
- Workflow must be **started manually** each time
- All data is **lost** after session ends
- **No token needed** — serveo.net is free forever

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
