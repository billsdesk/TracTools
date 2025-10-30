<p align="center">
  <img src="https://github.com/billsdesk/TracTools/blob/main/tractools-banner.png?raw=true" 
       alt="Trac Management Utilities Banner" width="800">
</p>

<h1 align="center">Trac Management Utilities</h1>

<p align="center">
  Simplifying <a href="https://trac.edgewall.org/">Trac</a> administration for single-user and local environments.
</p>

---

## 🧰 Overview

A collection of scripts and configuration tools that extend and simplify Trac administration for personal or lightweight deployments.

Includes:

- 🖥️ `tracserve` — command-line manager for start/stop, backup, restore, delete, and ticket date edits  
- ✉️ HTML email notification enhancements  
- 🗓️ Created-date editor for ticket history preservation  

---

## ✨ Features

- Start, stop, and restart Trac easily  
- Change ticket **created date** safely (supports ranges and lists)  
- Permanently delete tickets with safety checks and logging  
- Automated backups with retention and restore functions  
- Local timezone handling  
- Lightweight, single-script management (no plugins required)  

---

## ⚙️ Requirements

| Component | Version | Notes |
|------------|----------|--------|
| macOS / Linux | — | Tested on macOS 14+ |
| Python | ≥ 3.12 | |
| Trac | 1.6 | |
| SQLite | — | Default backend |
| Genshi | — | For HTML templates |

---

## 🚀 Quick Start

```bash
~/bin/tracserve start
~/bin/tracserve backup
~/bin/tracserve set-created 12-15 2024-01-05
~/bin/tracserve delete 20,21,22
```

---

## 🧩 Components

| Component | Purpose |
|------------|----------|
| `tracserve` | Command-line utility for Trac management (backups, restores, timestamps, deletes) |
| `html_email_plugin` | Enables HTML-formatted email notifications |
| `docs/` | Installation, backup, and usage guides |

---

## 📦 Recommended Directory Layout

```
~/Trac/
├── myproject/               ← Your Trac environment
│   ├── conf/
│   ├── db/
│   ├── log/
│   ├── templates/
│   └── TracConfig
├── tracenv/                 ← Python virtual environment
└── TracBackups/             ← Backup directory

~/bin/
└── tracserve                ← Management script (in your PATH)
```


---

## 🧠 Example Workflow

```bash
tracserve restart

🔄 Restarting Trac...
🛑 Stopping Trac...
✅ Trac stopped.
🧠 Virtual environment active: /Users/you/tracenv
🚀 Starting Trac on port 8080...
✅ Started Trac (PID 81679) → http://127.0.0.1:8080/
```

```bash
tracserve backup

💾 Creating backup...
✅ Backup complete: ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
```

```bash
tracserve set-created 30-34 2025-10-01

🧠 Virtual environment active: /Users/you/tracenv
📝 Setting created date to '2025-10-01 09:00:00' for tickets: 30 31 32 33 34
✅ Updated ticket #30
✅ Updated ticket #31
✅ Updated ticket #32
✅ Updated ticket #33
✅ Updated ticket #34
```

---

## 🪄 Command Reference

| Task | Command |
|------|----------|
| Start Trac | `tracserve start` |
| Stop Trac | `tracserve stop` |
| Restart Trac | `tracserve restart` |
| Create a backup | `tracserve backup` |
| Restore from backup | `tracserve restore <file>` |
| Change ticket creation date | `tracserve set-created <id>[,<id2>] <YYYY-MM-DD>` |
| Delete tickets (with confirmation) | `tracserve delete [--force] <id>[,<id2>]` |
| View logs | `tracserve view-log trac|tracserve <count>` |

---

## 🧾 Summary

✅ Self-contained Trac management toolkit  
✅ Safe delete, restore, and modify functions  
✅ HTML-formatted notifications  
✅ macOS/Linux friendly Bash scripting  
✅ Simple, modern command-line interface  

---

## 📚 Documentation

| Document | Description |
|-----------|--------------|
| [TracServe.md](docs/TracServe.md) | Complete command reference |
| [BackupRestore.md](docs/BackupRestore.md) | Backup and restore usage guide |
| [HTML_Email_Plugin.md](docs/HTML_Email_Plugin.md) | HTML email notification setup |
| [InstallationGuide.md](docs/InstallationGuide.md) | Installation and configuration steps |

---

## 📄 License
This project is licensed under the **BSD 3-Clause License** — see LICENSE.md for details.

---

## 💬 Author
Developed by **Bill Stackhouse**  
“Making Trac simpler, faster, and more maintainable.”
