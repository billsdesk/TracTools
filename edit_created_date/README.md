## Trac HTML Email Plugin
### Overview

By default, Trac does not allow modification of a ticket’s creation timestamp (time field) after it’s created.
This utility adds a controlled way to modify ticket creation dates — for example, when entering historic tickets to document past work.

It provides two mechanisms:

Method	Description	Recommended
🖥️ tracscript set-created	Command-line utility to safely edit creation date in the database	✅ Best choice
🌐 edit_created_date.py plugin	Experimental browser-based UI widget	Optional (not needed if using tracscript)


### System Requirements
Component	Version	Notes
Python	3.12+	Tested with Python 3.12.6
Trac	1.6	Required
SQLite	3.40+	or compatible database backend
tracscript	latest version	Installed in your Trac environment root


### Command-Line Date Editing

The simplest, safest way to modify ticket creation times is using tracscript.

### 🧠 Prerequisite

Make sure your TracConfig config file exists in ~/Trac/TracConfig and points to your environment.


Example contents:

~~~
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
~~~

### Usage Example

Change ticket #7 to have a created date of January 1, 2025 at 9:00 AM local time:

~~~
tracscript set-created 7 2025-01-01
~~~

Output example:

~~~
🧠 Virtual environment active: ~/tracenv
📝 Setting ticket #7 created date to '2025-01-01 09:00:00' ...
✅ Updated ticket #7: created timestamp changed successfully.
~~~

### Technical Notes
✅ What It Does

Converts your local date (e.g. 2025-01-01) to UTC microseconds (Trac’s internal format)

Updates the ticket.time field in the Trac database directly

Logs the change for traceability (no other fields modified)

### ⚙️ Command Internals (simplified)

~~~
from datetime import datetime, timezone
from trac.util.datefmt import to_utimestamp
from trac.env import open_environment

env = open_environment(project_dir)
db = env.get_read_db()

# Convert to UTC microseconds
dt = datetime(2025, 1, 1, 9, 0, 0).astimezone(timezone.utc)
ts = to_utimestamp(dt)

with env.db_transaction as db:
    db("UPDATE ticket SET time=%s WHERE id=%s", (ts, 7))
~~~

### 🧩 Safety

Only the ticket table’s time column is modified

Attachments, comments, and changelog entries are not affected (they key on ticket.id)

The Trac web UI will automatically reflect the new date

### Confirming the Change

You can verify directly in the Trac database using DBVisualizer, SQLite CLI, or Python:

~~~
SELECT id, summary, time, changetime FROM ticket WHERE id = 7;
~~~

Expected result:

~~~
id | summary | time (microseconds UTC) | changetime
---+----------+------------------------+------------
7  | Test2   | 1761939600000000        | 1761595336875139
~~~

Then open the ticket in Trac — the tooltip will display your local time, even though it’s stored internally as UTC.

### Optional: Browser Edit Plugin

If you want to enable in-browser editing (experimental):

Copy the plugin to your Trac project:

~~~
~/Trac/myproject/plugins/edit_created_date.py
~~~

Enable it in trac.ini:

~~~
[components]
edit_created_date.* = enabled
~~~

Restart Trac:

~~~
tracscript restart
~~~

You’ll then see a small “Edit Created Date” field below the ticket description.
However, the CLI version (tracscript set-created) is more reliable and does not interfere with the Trac UI rendering pipeline.

### Known Limitations

| Limitation | Description | Workaround |
|-------------|--------------|-------------|
| Tooltip may show UTC | Trac internally uses UTC timestamps | Interpreted correctly in most browsers |
| Doesn’t change changelog timestamps | Expected behavior — changelog represents history | Leave as-is |
| No multi-ticket batch update | Only single-ticket edits supported | Use small shell loops if needed |


### Example Automation Loop

You can update multiple tickets easily:

~~~
for id in 7 8 9 10; do
  tracscript set-created $id 2025-01-01
done
~~~

### Troubleshooting

| Issue | Cause | Fix |
|--------|--------|-----|
| `can't subtract offset-naive and offset-aware datetimes` | Mixing timezone-aware and naive datetimes | Ensure `.astimezone(timezone.utc)` is used |
| `sqlite3.OperationalError: database is locked` | Trac is actively serving requests | Stop Trac before editing: `tracscript stop` |


Changes not showing	Cached page	Refresh ticket page or clear browser cache


### Verification Example

After a successful edit:

~~~
03:45:13 ~: tracscript set-created 7 2025-01-01
🧠 Virtual environment active: /Volumes/Users/Bill/tracenv
📝 Setting ticket #7 created date to '2025-01-01 09:00:00' ...
✅ Updated ticket #7: created timestamp changed successfully.
~~~

Then check via the web UI:

~~~
Ticket creation date reads as Jan 1, 2025 9:00 AM (local)
~~~

No data loss, attachments still visible, workflow intact

### Credits

Developed and tested by Bill Stackhouse, with scripting and compatibility enhancements by ChatGPT (GPT-5).
Designed for Trac 1.6 with SQLite and macOS-based virtual environments.

Clean, robust, and minimal — no database risk, no UI patching.
