# 🛠️ Installation Guide — TracServe and Trac Management Utilities

This guide explains how to install, configure, and use **TracServe** and related tools for managing your local Trac environment.

---

## 📋 Prerequisites

Ensure the following are installed on your system:

| Requirement | Minimum Version | Notes |
|--------------|-----------------|--------|
| macOS or Linux | — | Tested on macOS 14+ |
| Python | 3.12+ | Use `python3 --version` to verify |
| Trac | 1.6 | Installed via pip inside virtual environment |
| Genshi | — | Required for HTML templates |
| SQLite | — | Default Trac backend supported |

---

## 📦 Installation Steps

### 1. Clone the Repository

```bash
cd ~/Trac
git clone https://github.com/billsdesk/TracTools.git
```

This creates:

```
~/Trac/TracTools/
```

---

### 2. Create Your Trac Environment

If you don’t already have a Trac project, create one:

```bash
mkdir -p ~/Trac/myproject
cd ~/Trac/myproject
trac-admin . initenv "My Project" sqlite:db/trac.db
```

---

### 3. Set Up a Python Virtual Environment

```bash
cd ~/Trac
python3 -m venv tracenv
source tracenv/bin/activate
pip install trac genshi
```

💡 You can confirm Trac is installed correctly:

```bash
tracd --version
```

---

### 4. Configure TracServe

Create a file named `TracConfig` in your Trac project directory:

```bash
nano ~/Trac/TracConfig
```

Add the following content:

```bash
# Trac configuration for tracserve
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
```

Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).

---

### 5. Test TracServe

Run the following from your TracTools directory:

```bash
cd ~/Trac/TracTools
./tracserve start
```

You should see:

```
🧠 Virtual environment active: /Users/you/tracenv
🚀 Starting Trac on port 8080...
✅ Started Trac (PID 12345) → http://127.0.0.1:8080/
```

Open your browser and visit:

👉 [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

---

### 6. Stop or Restart Trac

```bash
tracserve stop
tracserve restart
```

Example output:

```
🔄 Restarting Trac...
🛑 Stopping Trac...
✅ Trac stopped.
🚀 Starting Trac on port 8080...
✅ Started Trac (PID 67890) → http://127.0.0.1:8080/
```

---

## 🧠 Environment Layout

```
~/Trac/
├── myproject/               ← Your Trac environment
├── tracenv/                 ← Python virtual environment
├── TracBackups/             ← Backup storage
└── TracTools/               ← Management tools (tracserve, plugins, docs)
```

---

## 🧩 Optional Enhancements

| Feature | Description | Documentation |
|----------|--------------|----------------|
| HTML Email Plugin | Enables HTML-formatted Trac notifications | [HTML Email Plugin](HTML_Email_Plugin.md) |
| Backup & Restore | Automatic timestamped Trac backups | [Backup & Restore](BackupRestore.md) |
| Created Date Editor | Adjust ticket creation dates easily | [TracServe Guide](TracServe.md) |

---

## ✅ Verification Checklist

- [x] Virtual environment created (`~/Trac/tracenv`)  
- [x] `TracConfig` file present in `~/Trac/`  
- [x] TracServe runs without errors  
- [x] Backup and restore tested successfully  
- [x] Accessible via browser at `http://127.0.0.1:8080`  

---

## 🗒️ Notes

If you encounter errors like:
```
sqlite3.OperationalError: database is locked
```
Stop Trac before editing tickets or running `backup` or `restore` commands.

---

### 📚 Related Documentation
- [TracServe Command Reference](TracServe.md)
- [Backup & Restore](BackupRestore.md)
- [HTML Email Plugin](HTML_Email_Plugin.md)
