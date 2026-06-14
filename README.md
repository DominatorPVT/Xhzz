# 🖥️ Free VPS using GitHub & GitLab Actions

> A college project that turns CI/CD pipelines into a free Linux server using ngrok tunneling.

---

## 📌 What is this?

GitHub aur GitLab dono free cloud runners dete hain jo Linux machine chalate hain.
Is project me hum un machines ko **SSH-accessible VPS** ki tarah use karte hain — bilkul free! 🎉

---

## ⚙️ How it works

```
GitHub/GitLab Action trigger
        ↓
Ubuntu runner start hota hai
        ↓
SSH server install & configure
        ↓
ngrok se public tunnel banta hai
        ↓
IP + Port logs me dikhta hai
        ↓
Tum SSH se connect karo! 🚀
```

---

## 🚀 Setup Steps

### 1. ngrok Account banao
- [ngrok.com](https://ngrok.com) pe free account banao
- Dashboard se **Authtoken** copy karo

### 2. GitHub me Secret add karo
```
Settings → Secrets and variables → Actions → New secret

Name  : NGROK_TOKEN
Value : (apna ngrok token)
```

### 3. GitLab me Variable add karo
```
Settings → CI/CD → Variables → Add variable

Key   : NGROK_TOKEN
Value : (apna ngrok token)
```

### 4. Action/Pipeline manually trigger karo
- GitHub: `Actions tab → Free VPS Server → Run workflow`
- GitLab: `CI/CD → Pipelines → Run Pipeline`

---

## 📋 Credentials

| Field    | Value              |
|----------|--------------------|
| Username | `vpsuser`          |
| Password | `Vps@2024#Secure`  |

SSH command logs me dikhega — kuch aisa:
```bash
ssh -p 12345 vpsuser@0.tcp.ngrok.io
```

---

## ⏰ Session Time

| Platform | Free Time     |
|----------|---------------|
| GitHub   | ~5 hours 50 min |
| GitLab   | ~5 hours 50 min |

> Jab chahiye tab manually trigger karo — automatic kuch nahi hoga! 😄

---

## 📁 Project Structure

```
free-vps/
├── .github/
│   └── workflows/
│       └── vps.yml        # GitHub Actions workflow
├── .gitlab-ci.yml         # GitLab CI pipeline
└── README.md              # Yeh file 😄
```

---

## ⚠️ Limitations

- Session ~6 hours max hoti hai (CI/CD limit)
- ngrok free me sirf 1 tunnel allowed hai
- GitLab me shared runners ke liye card verify karna padta hai
- Data persist nahi hota (session end = sab reset)

---

## 💡 Use Cases (College Project Ideas)

- Host a Node.js / Python web app temporarily
- Run scripts on a Linux environment
- Test server-side code without buying VPS
- Learn Linux commands hands-on

---

## 🧑‍💻 Tech Used

- **GitHub Actions** — CI/CD runner
- **GitLab CI** — alternate CI/CD runner  
- **Ubuntu 22.04** — runner OS
- **OpenSSH** — SSH server
- **ngrok** — TCP tunnel for public access

---

## 📜 License

MIT License — free to use, modify, share! 🤝

---

*Made with curiosity and GitHub's free compute 😎*
