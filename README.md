<div align="center">

# ⚡ Action VPS

**Free temporary Ubuntu VPS via GitHub Actions & GitLab CI**

[![Stars](https://img.shields.io/github/stars/DominatorStufs/action-vps?style=for-the-badge&color=yellow)](https://github.com/DominatorStufs)
[![Forks](https://img.shields.io/github/forks/DominatorStufs/action-vps?style=for-the-badge&color=blue)](https://github.com/DominatorStufs)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

**Action VPS** gives you a temporary Ubuntu environment running inside GitHub Actions or GitLab CI — with SSH access and a public ngrok tunnel (hostname + port).

> ⚠️ This is **not** a real VPS. It runs for ~6 hours per session and resets every time.

---

## 🔑 Step 1 — Get Your Ngrok Token

1. Go to 👉 [https://ngrok.com](https://ngrok.com)
2. Sign up / Log in (free account)
3. Go to **Dashboard → Your Authtoken**
4. Copy your token

> It looks like: `2abc123XYZ_xxxxxxxxxxxxxxxxxxxxxxxx`

---

## 🔐 Step 2 — Add Token to GitHub Secret

1. Open your **forked repo** on GitHub
2. Go to **Settings**

```
Settings → Secrets and variables → Actions → New repository secret
```

3. Fill in:

```
Name  : NGROK_TOKEN
Value : (paste your ngrok authtoken here)
```

4. Click **Add secret** ✅

---

## 🔐 Step 2 (GitLab) — Add Token to GitLab CI Variable

1. Open your **GitLab project**
2. Go to:

```
Settings → CI/CD → Variables → Add variable
```

3. Fill in:

```
Key   : NGROK_TOKEN
Value : (paste your ngrok authtoken here)
```

4. Click **Add variable** ✅

---

## 🚀 Step 3 — Run the VPS

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

---

## 🔌 Step 4 — Connect via SSH

Use any SSH client (**Terminus**, **JuiceSSH**, **PuTTY**, **Termux**).

```
Host     → (HOST from logs)
Port     → (PORT from logs)
Username → (USERNAME from logs)
Password → (PASSWORD from logs)
```

### Termux / Terminal command:

```bash
ssh USERNAME@HOST -p PORT
```

---

## 📦 Features

| Feature | Details |
|---|---|
| 🐧 OS | Ubuntu (latest) |
| 🔐 SSH | Random username & password |
| 🌐 Tunnel | ngrok (real hostname + port in logs) |
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
- **Credentials change** on every run
- Workflow must be **started manually** each time
- All data is **lost** after session ends
- ngrok free plan allows **1 tunnel** at a time

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
