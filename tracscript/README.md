##⚙️ tracscript — Trac Environment Management Tool
###Overview

tracscript is a bash-based management utility that simplifies running and maintaining your Trac environment.
It provides a clean command-line interface for starting, stopping, backing up, restoring, and managing Trac — including a custom ticket date utility.

It’s designed to make Trac administration Mac-friendly and maintainable, without requiring deep system integration.

###🚀 Quick Commands
Command	Description
tracscript start	Start the Trac server
tracscript stop	Stop the Trac server
tracscript restart	Restart Trac
tracscript backup	Create a timestamped backup (keeps the 5 most recent)
tracscript restore <file>	Restore a backup from file
tracscript set-created <id> <YYYY-MM-DD>	Update a ticket’s created date (defaults time to 09:00)
tracscript help	Display this help summary
###🧩 Configuration File

tracscript reads its configuration from a simple text file named:

TracConfig


(located in your Trac project directory)

Example contents:

~~~
# Trac configuration for tracscript
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
~~~

💡 All paths are absolute and should use $HOME instead of /Users/<name> for portability.

###🧠 Virtual Environment Integration

tracscript automatically activates your Trac Python virtual environment when running commands.

Each action confirms activation, for example:

~~~
🧠 Virtual environment active: /Users/you/tracenv
~~~

This ensures trac-admin, Trac libraries, and database operations all use the correct environment.

###💾 Backup System

tracscript backup automatically creates compressed backups containing:

Your entire Trac project environment (myproject/)

Your configuration files

Your templates and plugins

A copy of your tracscript for version tracking

Backups are saved to:

~~~
$HOME/Trac/TracBackups/
~~~

and named like:

20251027-152837-TracBackup.tar.gz


Old backups beyond the 5 most recent are automatically deleted:

🧹 Pruning old backups (keeping 5 most recent)...

###🔁 Restore

To restore a previous backup:

~~~
tracscript restore /Users/you/Trac/TracBackups/20251027-152837-TracBackup.tar.gz
~~~

The restore process will not overwrite:

Your virtual environment (tracenv)

Your tracscript or other tools

The current Trac instance must be stopped before running restore.

⚡ Example Session

~~~
tracscript restart

🔄 Restarting Trac...
🛑 Stopping Trac (PID 81630)...
✅ Trac stopped.
🧠 Virtual environment active: /Users/you/tracenv
🚀 Starting Trac on port 8080...
✅ Started Trac (PID 81679) → http://127.0.0.1:8080/
~~~

~~~
tracscript backup
💾 Creating backup at /Users/you/Trac/TracBackups/20251027-152837-TracBackup.tar.gz ...
✅ Backup complete!
~~~

###🧾 Summary

✅ Start, stop, restart Trac easily

✅ Auto-activates the virtual environment

✅ Timestamped backups with automatic pruning

✅ Safe restores

✅ Built-in ticket creation date editor

✅ Mac-friendly and portable

###📦 Recommended Directory Layout

~~~
~/Trac/
├── myproject/
│   ├── conf/
│   ├── db/
│   ├── log/
│   ├── templates/
│   ├── TracConfig         ← Project config for tracscript
├── tracenv/               ← Python virtual environment
├── TracBackups/           ← Automated backups
└── TracTools/
    └── tracscript         ← This script
~~~