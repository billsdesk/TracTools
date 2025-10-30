# 💾 Backup & Restore — TracServe Utility

This guide explains how to back up and restore your Trac environment safely using **tracserve**.

Backups are fully automated, timestamped, and pruned to keep only the most recent five copies.

---

## 🧰 Overview

tracserve ensures your Trac project and configuration are safely backed up, including:

- Full Trac project environment (configuration, database, templates, plugins)
- A copy of your `TracConfig` file
- A copy of the `tracserve` script for version tracking

Your Python virtual environment (`tracenv`) is **not** included in backups.  
This ensures faster operation and avoids dependency conflicts during restoration.

---

## 📦 Directory Layout

```
~/Trac/
├── myproject/               ← Your active Trac environment
├── tracenv/                 ← Python virtual environment (not backed up)
├── TracBackups/             ← Backup storage location
└── TracTools/
    └── tracserve
```

---

## 💾 Creating a Backup

To create a new backup, simply run:

```bash
tracserve backup
```

Example output:

```
🧠 Virtual environment active: /Users/you/tracenv
💾 Creating backup at ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz ...
✅ Backup complete!
🧹 Pruning old backups (keeping 5 most recent)...
   🗑️  Removing /Users/you/Trac/TracBackups/20251025-121002-TracBackup.tar.gz
```

Backups are stored as compressed `.tar.gz` files named with a timestamp:

```
~/Trac/TracBackups/YYYYMMDD-HHMMSS-TracBackup.tar.gz
```

---

## ♻️ Restoring a Backup

Restoring is just as simple — use the `restore` command:

```bash
tracserve restore ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
```

Example output:

```
🧠 Virtual environment active: /Users/you/tracenv
📦 Restoring backup from ~/Trac/TracBackups/20251027-152837-TracBackup.tar.gz ...
✅ Restore complete.
🚫 Skipped restoring tracenv and tracserve script (safety mode)
```

### 🧩 Safety Rules

- The restore process does **not** overwrite your `tracserve` script or `tracenv`.  
- You must stop the Trac server before restoring:

```bash
tracserve stop
tracserve restore <backup-file>
tracserve start
```

---

## 🗒️ Notes

| Limitation | Description | Workaround |
|-------------|--------------|-------------|
| Backup size may vary | Larger databases produce larger `.tar.gz` files | Use external compression utilities if needed |
| Active Trac instance may lock DB | SQLite may lock the file if Trac is running | Stop Trac before backing up |
| Retention limited to 5 backups | To prevent disk growth | Adjust limit in script if needed |

---

## 📚 Related Documentation

- [TracServe Command Reference](TracServe.md)
- [Installation Guide](InstallationGuide.md)
- [HTML Email Plugin](HTML_Email_Plugin.md)
