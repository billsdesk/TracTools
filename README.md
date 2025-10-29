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

- 🖥️ `tracserve` — command-line manager for start/stop, backup, restore, ticket date edits, and safe ticket deletion  
- ✉️ HTML email notification enhancements  
- 🗓️ Created-date editor for ticket history preservation  

---

## ✨ Features

- HTML-formatted ticket notifications  
- Change ticket **created date(s)** safely  
- Delete tickets with confirmation or `--force` override  
- Automated backups (with retention)  
- Simple restore workflow  
- Unified action logging (`tracserve.log`)  
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

```bash
# Run from your Trac directory
tracserve start
tracserve backup
tracserve set-created 12 2024-01-05
```

---

## 📂 Recommended Directory Layout

```text
~/Trac/
├── myproject/
│   ├── conf/
│   ├── db/
│   ├── log/
│   ├── templates/
│   ├── TracConfig          ← Project config for tracserve
├── tracenv/                ← Python virtual environment
├── TracBackups/            ← Automated backups and tracserve.log
└── TracTools/
    └── tracserve           ← This script
```

---

## 🧩 Configuration

`tracserve` reads its settings from:

```bash
$HOME/Trac/TracConfig
```

Example contents:

```bash
# Trac configuration for tracserve
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
```

💡 Use `$HOME` instead of `/Users/<name>` for portability.

---

## ⚙️ Command Reference

```bash
Usage: tracserve <command> [options]

Commands:
  start                          Start the Trac server
  stop                           Stop the Trac server
  restart                        Restart the Trac server
  backup                         Create a timestamped backup (keeps 5 most recent)
  restore <file>                 Restore a backup (safe mode)
  set-created <ids> <date>       Update one or more tickets' created date(s)
  delete [--force|-f] <ids>      Delete one or more tickets (with confirmation)
  view-log [trac|tracserve] [N]  View either the Trac or tracserve log (default 20 lines)
  help                           Show this help message

Examples:
  tracserve set-created 12-14,20 2025-08-01
  tracserve delete --force 10,11,12
```

---

## 🧠 Virtual Environment Integration

When executing, `tracserve` automatically activates your Trac Python virtual environment.

Example:

```bash
🧠 Virtual environment active: /Users/you/tracenv
```

This ensures all commands use the correct `trac-admin`, Trac libraries, and database context.

---

## 💾 Backup System

Backups include:

- Your entire Trac environment (`myproject/`)
- Configuration and templates
- A copy of your `tracserve` script
- Retains the 5 most recent backups

Example:

```bash
tracserve backup
💾 Creating backup...
✅ Backup complete: ~/Trac/TracBackups/20251029-152837-TracBackup.tar.gz
```

Older backups are automatically pruned.

---

## 🔁 Restore

Restore a previous backup safely:

```bash
tracserve restore ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
```

This does **not** overwrite:
- The virtual environment (`tracenv`)
- The current `tracserve` script
- Active configuration files

---

## 🗓️ Multi-Ticket Date Editing

You can set the “created” date for one or multiple tickets:

```bash
tracserve set-created 34,35,36 2025-10-01
tracserve set-created 10-15 2025-09-01
```

✅ Supports:
- Comma-separated IDs  
- Ranges (e.g., `10-15`)  
- Combined input (`10-12,20,25-28`)

Each change is logged automatically in `tracserve.log`.

---

## 🗑️ Safe Ticket Deletion

Delete one or multiple tickets:

```bash
tracserve delete 35,36
```

`tracserve` will confirm before deletion unless `--force` is specified:

```bash
tracserve delete --force 30-34
```

Deleted tickets and timestamps are recorded in `tracserve.log`.

---

## 🪵 Viewing Logs

`tracserve` can display either its own action log or Trac’s main server log.

| Command | Description |
|----------|-------------|
| `tracserve view-log` | Show last 20 entries from tracserve log |
| `tracserve view-log tracserve 100` | Show last 100 entries from tracserve log |
| `tracserve view-log trac 50` | Show last 50 lines of Trac’s log file |

### Log Locations

| Log | Path | Contents |
|------|------|-----------|
| Tracserve Log | `$BACKUP_PATH/tracserve.log` | Ticket deletions, created date changes, and script actions |
| Trac Log | `$TRAC_PROJECT_PATH/log/trac.log` | Internal Trac operations and plugin events |

Example:

```
📜 Showing last 40 entries from tracserve log:
   /Users/bill/Trac/TracBackups/tracserve.log
---------------------------------------------
2025-10-29 14:10:24 | user=bill | SET-CREATED: ticket #42 → 2025-01-01 09:00:00
2025-10-29 14:15:01 | user=bill | DELETE: ticket #43
```

---

## ✅ Summary of Enhancements

| Command | Description |
|----------|-------------|
| `tracserve set-created <ids> <YYYY-MM-DD>` | Update ticket “created” date(s) and log the change |
| `tracserve delete <ids>` | Delete ticket(s) safely and log the deletion |
| `tracserve view-log [trac|tracserve] [N]` | View logs from either tracserve or Trac |
| `tracserve backup` | Create a timestamped backup with automatic retention |
| `tracserve restore <file>` | Restore safely without overwriting your environment |

---

## 📄 License

This project is licensed under the BSD 3-Clause License — see `LICENSE.md` for details.

---

## 💬 Author

Developed by **Bill Stackhouse**  
“Making Trac simpler, faster, and more maintainable.”
