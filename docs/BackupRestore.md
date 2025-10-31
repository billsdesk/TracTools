
## 💾 Backup and Restore

`tracserve` includes a simple but powerful backup and restore system that preserves your
entire Trac project and configuration while protecting your virtual environment (`tracenv`).

### 🔒 Safe Backups

Backups now store **relative paths** (no `/Volumes/...` nesting) so they can be restored
cleanly on any machine.

Each backup archive includes:
- `Trac/myproject` — your full Trac environment (database, attachments, config)
- `Trac/TracConfig` — script configuration file
- `bin/tracserve` — a copy of the running management script for version traceability
- *(optionally)* `Trac/tracenv` — only if you choose to include it manually

Example command:
```bash
tracserve backup
```

Output:
```
💾 Creating backup at ~/Trac/TracBackups/20251030-150153-TracBackup.tar.gz ...
✅ Backup complete!
🧹 Pruning old backups (keeping 5 most recent)...
```

Backups are stored in:
```
~/Trac/TracBackups/
```
and automatically rotated, keeping only the 5 most recent.

---

### ♻️ Restoring from Backup

Restores are **safe and non-destructive** — `tracenv` is never overwritten.

Example:
```bash
tracserve restore ~/Trac/TracBackups/20251030-150153-TracBackup.tar.gz
```

During restore, `tracserve`:
1. Stops any running Trac instance (via PID file).  
2. Extracts the selected backup relative to your home directory (`~/Trac/...`).  
3. Skips `Trac/tracenv` entirely for safety.  
4. Restores `myproject`, `TracConfig`, and `bin/tracserve`.  

Example output:
```
♻️  Preparing to restore from backup: ~/Trac/TracBackups/20251030-150153-TracBackup.tar.gz
🛑 Stopping running Trac instance...
📦 Extracting backup...
✅ Restore complete!
💡 Note: tracenv was intentionally NOT restored (for safety).
```

---

### 🧠 Notes

| Behavior | Description |
|-----------|--------------|
| **Relative paths** | Backups now use relative paths from `~/`, avoiding `/Volumes/...` nesting. |
| **Safe restores** | Restores do not overwrite the virtual environment. |
| **Version capture** | Each backup includes a copy of the `tracserve` script. |
| **Automatic pruning** | Only the 5 newest backups are retained. |

💡 *To restart Trac after restoring:*
```bash
~/bin/tracserve restart
```
