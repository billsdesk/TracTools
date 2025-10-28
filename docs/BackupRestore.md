# 💾 Backup and Restore Guide

This document explains how to **back up** and **restore** your Trac environment using the `tracscript` management tool.

---

## 🧠 Overview

`tracscript` automates Trac maintenance with timestamped backups, automatic pruning, and safe restores.  
Backups include your Trac project environment, configuration, templates, and scripts.

---

## ⚙️ Backup

To create a backup:

```bash
tracscript backup
```

This will:

- Compress your Trac project (`myproject/`)  
- Include templates, configuration, and the `tracscript` itself  
- Save the archive under:

```
$HOME/Trac/TracBackups/
```

Backups are named automatically, for example:

```
20251027-152837-TracBackup.tar.gz
```

---

### 🧹 Automatic Pruning

`tracscript` keeps only the **five most recent backups** and deletes older ones automatically:

```
🧹 Pruning old backups (keeping 5 most recent)...
```

---

## 🔁 Restore

To restore from a backup archive:

```bash
tracscript restore $HOME/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
```

This will:

- Stop Trac (if running)  
- Extract your environment into the correct project path  
- Preserve your virtual environment (`tracenv`)  
- Preserve your management scripts and tools  

---

## ⚠️ Notes

| Limitation | Description | Workaround |
|-------------|--------------|-------------|
| Trac must be stopped | SQLite locks while active | Use `tracscript stop` before restoring |
| Virtual environment not restored | Keeps your Python setup safe | Recreate manually if needed |
| Backup path not found | Directory missing or misconfigured | Verify `BACKUP_PATH` in `TracConfig` |

---

**Author:** Bill Stackhouse  
**Part of:** [TracTools](https://github.com/billsdesk/TracTools)
