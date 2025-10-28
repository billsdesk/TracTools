# Backup & Restore

The `tracscript` utility provides built-in backup and restore capabilities.

## Backup

~~~
tracscript backup
~~~

Creates a timestamped archive containing:

* Entire Trac project directory

* Virtual environment (tracenv)

* The tracscript itself

Archives are saved in:

~~~
/Volumes/Users/Bill/Trac/TracBackups
~~~

Only the 5 most recent backups are kept automatically.

### Restore

~~~
tracscript restore /path/to/backup.tar.gz
~~~

Restores only the Trac project (skips restoring the script and tracenv).

💡 Tip: Backups are self-contained. You can restore them on another system by recreating your
virtual environment and placing the project folder in the same relative location.