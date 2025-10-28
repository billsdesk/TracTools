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

- 🖥️ `tracscript` — command-line manager for start/stop, backup, restore, and ticket date edits  
- ✉️ HTML email notification enhancements  
- 🗓️ Created-date editor for ticket history preservation  

---

## ✨ Features

- HTML-formatted ticket notifications  
- Change ticket **created date** safely  
- Automated backups (with retention)  
- Simple restore workflow  
- Local timezone handling  
- Clean, minimal Bash automation  

---

## ⚙️ Requirements

- macOS or Linux  
- Python ≥ 3.12  
- Trac 1.6  
- SQLite backend  
- Genshi (for HTML templates)  
- Configured Trac environment (`tracd` compatible)  

---

## 🚀 Quick Start

~~~
# Run from your Trac directory
./scripts/tracscript start
./scripts/tracscript backup
./scripts/tracscript set-created 12 2024-01-05
~~~

### 📂 Repository Structure

~~~
TracTools/
├── docs/                 → Additional documentation
├── edit_created_date/    → Ticket creation date plugin
├── html_email_plugin/    → HTML email notification system
├── tracscript/           → Main management script
├── LICENSE.md
└── README.md
~~~

### 🧩 Components

Component	Purpose
tracscript	Command-line tool to manage Trac, backups, restores, and timestamps
html_email_plugin	Enables HTML-formatted email notifications
edit_created_date	Allows safe modification of ticket “created” timestamps
docs/	Contains detailed setup and reference documentation

### 🧠 Example Workflow

~~~
tracscript restart

🔄 Restarting Trac...
✅ Started Trac → http://127.0.0.1:8080/
~~~

~~~
tracscript backup

💾 Creating backup...
✅ Backup complete: ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
~~~

### 🪄 Tips

| Task | Command |
|------|----------|
| Start Trac | `tracscript start` |
| Stop Trac | `tracscript stop` |
| Restart Trac | `tracscript restart` |
| Create a backup | `tracscript backup` |
| Restore from backup | `tracscript restore <file>` |
| Change ticket creation date | `tracscript set-created <id> <YYYY-MM-DD>` |

## 📄 License
This project is licensed under the BSD 3-Clause License — see LICENSE.md for details.

## 💬 Author
Developed by Bill Stackhouse

“Making Trac simpler, faster, and more maintainable.”
