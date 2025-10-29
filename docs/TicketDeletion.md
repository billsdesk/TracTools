# 🗑️ Ticket Deletion

Adds a **Delete** button directly to the Trac ticket interface,  
allowing easy removal of test or obsolete tickets.

---

### 🔧 How It Works

Once enabled, a **Delete** button appears at the bottom of each ticket, next to the **Reply** button.  

When clicked:
- The selected ticket is permanently removed.  
- All **comments**, **attachments**, and **changelog entries** associated with it are deleted.  
- The action is logged in Trac’s `trac.log` file for traceability.

---

### 🛠️ Enabling the Delete Button

To activate this feature:

1. **Copy the plugin** file (usually named `ticket_delete.py`) into your Trac environment’s plugin folder:

   ```bash
   cp tracscript/plugins/ticket_delete.py ~/Trac/myproject/plugins/
Restart Trac to load the new plugin:

~~~
tracscript restart
~~~

Verify it’s loaded

Open any ticket and look for a – Delete button beside Reply.

### ⚠️ Important Notes

❗ Deletion is permanent. There is no undo or confirmation prompt.

💾 Always run a backup first:

~~~
tracscript backup
~~~

🧱 The delete feature affects only tickets and their associated content; it does not alter Trac configuration, users, or permissions.

🧠 Implementation Notes (Optional)
If you’d like to modify who can see the Delete button,
you can easily add a visibility condition to the plugin’s template or Python code.

Example placeholder for permission logic (not required by default):

~~~
# Optional check to limit visibility
# if 'TRAC_ADMIN' in req.perm:
#     show_delete_button()
~~~


### ✅ Summary


1.	Copy plugin	Place ticket_delete.py into your Trac plugins/ directory
2.	Restart Trac	Reloads the plugin so the Delete button appears
3.	Verify operation	Open a ticket and confirm – Delete is visible
4.	Backup first	Run tracscript backup before deleting
5.	Delete ticket	Click – Delete at the bottom of the ticket page

