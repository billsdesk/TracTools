# tracscript

`tracscript` is a Bash-based management utility for local Trac environments.

It simplifies routine Trac administration by providing one unified command for:

| Task | Command |
|------|----------|
| Start Trac | `tracscript start` |
| Stop Trac | `tracscript stop` |
| Restart Trac | `tracscript restart` |
| Create a backup | `tracscript backup` |
| Restore from backup | `tracscript restore <file>` |
| Change ticket creation date | `tracscript set-created <id> <YYYY-MM-DD>` |

---

### 🧠 Key Features
- Auto-activates your Python virtual environment  
- Safely updates ticket creation timestamps  
- Manages compressed backups with retention (default: 5)  
- Provides visual command-line feedback for each operation  
- Designed for macOS and Linux  

---

### ⚙️ Configuration
Reads settings from the file:
$HOME/Trac/TracConfig


Example:


~~~
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
~~~

---

✅ *Included in*: [TracTools](https://github.com/billsdesk/TracTools)  
📄 *License*: BSD 3-Clause
