# ⚙️ TracServe — Trac Environment Management Tool

`tracserve` is a lightweight Bash utility that simplifies managing your local Trac environment —  
from starting and stopping the server, to backups, restores, and ticket maintenance.

It’s designed to make Trac administration simple, safe, and Mac-friendly,  
without requiring additional plugins or system-level setup.

---

## 🧰 Overview

**tracserve** manages your Trac environment through a single command-line interface.  
It supports Trac maintenance tasks including:

- Starting and stopping the Trac server  
- Backing up and restoring the project safely  
- Changing ticket “created” timestamps  
- Deleting tickets (with confirmation and logging)  
- Viewing logs for both Trac and tracserve itself  

---

## 🚀 Quick Commands

| Command | Description |
|----------|--------------|
| `tracserve start` | Start the Trac server |
| `tracserve stop` | Stop the Trac server |
| `tracserve restart` | Restart Trac |
| `tracserve backup` | Create a timestamped backup (keeps last 5) |
| `tracserve restore <file>` | Restore from a backup safely |
| `tracserve set-created <ids> <YYYY-MM-DD>` | Update one or more ticket creation dates |
| `tracserve delete [--force] <ids>` | Delete one or more tickets |
| `tracserve view-log trac|tracserve [count]` | View either the Trac or tracserve log |
| `tracserve help` | Show this help summary |

---

## 🧩 Configuration

tracserve reads its configuration from a file named:

```
~/Trac/TracConfig
```

Example:

```bash
# Trac configuration for tracserve
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
```

💡 **Tip:** Use `$HOME` instead of `/Users/<name>` for portability.

---

## 🧠 Virtual Environment Integration

tracserve automatically activates your Trac Python environment for every command.

Example output:

```
🧠 Virtual environment active: /Users/you/tracenv
```

This ensures `trac-admin`, `tracd`, and all Trac operations run with the correct Python setup.

---

## 🗓️ Set Created Date

Update one or more ticket creation dates — individually or in ranges.

Examples:

```bash
tracserve set-created 15 2025-01-10
tracserve set-created 30,31,32 2025-02-01
tracserve set-created 40-45,50 2025-03-01
```

Example output:

```
🧠 Virtual environment active: /Users/you/tracenv
📝 Setting created date to '2025-03-01 09:00:00' for tickets: 40 41 42 43 44 45 50
✅ Updated ticket #40
✅ Updated ticket #41
✅ Updated ticket #42
✅ Updated ticket #43
✅ Updated ticket #44
✅ Updated ticket #45
✅ Updated ticket #50
```

---

## 🗑️ Delete Tickets

Delete one or more tickets safely. Confirmation is required unless using `--force`.

Examples:

```bash
tracserve delete 25
tracserve delete 12,14,15
tracserve delete 30-35 --force
```

Example output:

```
🧠 Virtual environment active: /Users/you/tracenv
⚠️  You are about to permanently delete the following tickets: 30 31 32 33 34 35
   Are you sure? (y/N): y
✅ Deleted tickets: 30,31,32,33,34,35
🗒️  Log entry recorded in ~/Trac/tracserve.log
```

---

## 📜 View Logs

You can view the recent lines of either the Trac or tracserve logs.

Examples:

```bash
tracserve view-log trac 30
tracserve view-log tracserve 15
```

Default (no count provided):

```
📄 Showing last 20 lines of tracserve.log
[2025-10-29 12:30] Updated ticket #40 created date
[2025-10-29 12:35] Deleted tickets: 30-34 (confirmed)
```

---

## 💾 Backup and Restore (Summary)

Create or restore backups of your Trac environment.  
Backups are timestamped and automatically pruned to keep the last five.

Examples:

```bash
tracserve backup
tracserve restore ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
```

Example output:

```
💾 Creating backup at ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz ...
✅ Backup complete!
🧹 Pruned old backups, keeping 5 most recent.
```

See [Backup & Restore](BackupRestore.md) for details.

---

## 🧾 Summary

✅ Start, stop, and restart Trac easily  
✅ Auto-activates your virtual environment  
✅ Backups and restores with retention  
✅ Ticket “created” date editing  
✅ Safe ticket deletion with logging  
✅ View both Trac and tracserve logs  

---

## 📦 Recommended Directory Layout

```
~/Trac/
├── myproject/
│   ├── conf/
│   ├── db/
│   ├── log/
│   ├── templates/
│   ├── TracConfig
├── tracenv/                 ← Python virtual environment
├── TracBackups/             ← Backup storage
└── TracTools/
    └── tracserve            ← This script
```

---

### 📚 Related Documentation
- [Installation Guide](InstallationGuide.md)
- [Backup & Restore](BackupRestore.md)
- [HTML Email Plugin](HTML_Email_Plugin.md)
