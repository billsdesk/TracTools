## ⚙️ tracscript — Trac Environment Management Tool

### Overview

`tracscript` is a bash-based management utility that simplifies running and maintaining your Trac environment.  
It provides a clean command-line interface for starting, stopping, backing up, restoring, and managing Trac —  
including a custom ticket date utility.

It’s designed to make Trac administration Mac-friendly and maintainable, without requiring deep system integration.

---

### 🚀 Quick Commands

| Command | Description |
|----------|-------------|
| `tracscript start` | Start the Trac server |
| `tracscript stop` | Stop the Trac server |
| `tracscript restart` | Restart Trac |
| `tracscript backup` | Create a timestamped backup (keeps the 5 most recent) |
| `tracscript restore <file>` | Restore a backup from file |
| `tracscript set-created <id> <YYYY-MM-DD>` | Update a ticket’s created date (defaults time to 09:00) |
| `tracscript help` | Display this help summary |

---

### 🧩 Configuration File

`tracscript` reads its configuration from a simple text file named:

