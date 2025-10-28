##🕓 Ticket Utilities — Set Ticket Creation Date

###Overview

This utility extends Trac with a command-line feature to update a ticket’s “created” date,
allowing you to retroactively record historical work or import older issues with accurate timestamps.

It integrates directly into the tracscript management tool (see /TracTools/tracscript).

###🧭 Why You Need It

By default, Trac does not allow editing the ticket creation date (time field).
This is inconvenient when migrating tickets or cataloging past work.

The set-created command provides a simple, safe way to modify that field without breaking Trac’s internal references or attachments.

###⚙️ Usage

~~~
tracscript set-created <ticket-id> <YYYY-MM-DD>
~~~

Example:

~~~
tracscript set-created 17 2024-05-10
~~~

This sets ticket #17’s created date to 2024-05-10 09:00:00 (local time),
and the timestamp is stored in UTC within the database.

###🔍 Output Example
🧠 Virtual environment active: /Users/<you>/tracenv

📝 Setting ticket #17 created date to '2024-05-10 09:00:00' ...

📂 Using Trac environment at: /Users/<you>/Trac/myproject

📅 Old created date: 2025-01-27 12:18:00 PST

📆 New created date: 2024-05-10 09:00:00 PST

✅ Updated ticket #17 successfully (stored as UTC)

###🧠 Implementation Notes

The script connects directly to your Trac environment database.

Updates only the time field in the ticket table.

All relationships (comments, attachments, etc.) remain intact — they are keyed by ticket ID, not timestamp.

Safe to run while Trac is active (uses transactional update).

###⚡ Advanced Details

Internally, the command:

Converts the provided local date/time to UTC.

Converts it to a Trac-compatible microsecond timestamp.

Executes:

~~~
UPDATE ticket SET time = ? WHERE id = ?
~~~

Confirms and logs the before/after values.

###🧩 Integration

Included as a built-in subcommand of:

~~~
tracscript
~~~

To view help:

~~~
tracscript help
~~~

###🧾 Summary

✅ Safely updates ticket creation timestamps

✅ Uses proper Trac timestamp format

✅ Keeps attachments, comments, and history intact

✅ Logs every change to console

✅ Fully integrated with the Trac environment and virtualenv
