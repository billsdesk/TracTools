# 🗑️ Ticket Deletion Feature

TracTools adds a Delete button directly to each ticket’s interface, allowing safe removal of unwanted or test tickets.

## 🔧 How It Works

Appears at the bottom of the ticket near the “Reply” button

Available only to users with administrative privileges

Deletes:

The ticket itself

All comments and attachments

Associated changelog entries

Logs the action in trac.log for auditing

## ⚠️ Important Notes

Deletions are permanent — there is no undo.

It’s strongly recommended to run a backup first:

~~~
tracscript backup
~~~
