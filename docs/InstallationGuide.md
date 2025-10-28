# ⚙️ Installation Guide

This guide explains how to install and configure **Trac Management Utilities** on macOS or Linux.

---

## 🧩 Requirements

- macOS or Linux  
- Python ≥ 3.12  
- Trac 1.6  
- SQLite backend  
- Genshi (for HTML templates)  
- A configured Trac environment (`tracd` compatible)

---

## 🪄 Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/billsdesk/TracTools.git
cd TracTools
```

---

### 2. Set Up the Virtual Environment

```bash
python3 -m venv $HOME/tracenv
source $HOME/tracenv/bin/activate
pip install trac genshi
```

---

### 3. Create Your Trac Environment

```bash
trac-admin $HOME/Trac/myproject initenv
```

---

### 4. Configure TracScript

In your Trac project directory, create a file named `TracConfig`:

```bash
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
```

---

### 5. Run TracScript Commands

Start your Trac instance:

```bash
tracscript start
```

Make a backup:

```bash
tracscript backup
```

Change a ticket creation date:

```bash
tracscript set-created 7 2025-01-01
```

---

## ✅ Verification

Visit your Trac instance in a browser:

```
http://127.0.0.1:8080/
```

You should see your environment loaded and ready.

---

**Author:** Bill Stackhouse  
**Part of:** [TracTools](https://github.com/billsdesk/TracTools)
