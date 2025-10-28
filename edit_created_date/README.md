# 🗓️ Set Ticket Created Date

This document explains how to safely modify a Trac ticket’s **created date** using the `tracscript set-created` command.  
It replaces the earlier plugin-based approach that attempted to provide a web UI.

---

## 🎯 Purpose

The `set-created` command allows administrators to update the `time` field in the Trac database for a ticket.  
This is useful when importing historical issues or aligning ticket creation dates with other systems.

---

## 🧠 Command Overview

```bash
tracscript set-created <ticket-id> <YYYY-MM-DD>
```

### Example

```bash
tracscript set-created 42 2025-01-01
```

This sets ticket **#42** to a created date of **January 1, 2025, at 09:00 local time**.

---

## 🧩 Behavior Details

- The command **stops Trac** before applying the change (recommended).  
- It writes the updated timestamp directly to the `ticket` table in your Trac SQLite database.  
- The stored time is always in **UTC**, but Trac will display it using your configured timezone.  
- No changes are made to changelog or comment timestamps.

---

## ⚠️ Notes and Limitations

| Issue | Cause | Workaround |
|-------|--------|-------------|
| Tooltip may show UTC | Trac stores timestamps internally as UTC | Interpreted correctly by browsers |
| Doesn’t update changelog times | Expected — changelog represents history | Leave as-is |
| No batch update | Command updates one ticket at a time | Use small shell loops if needed |

---

## 🧾 Example Session

```bash
tracscript set-created 7 2025-01-01
🧠 Virtual environment active: /Users/you/tracenv
📝 Setting ticket #7 created date to '2025-01-01 09:00:00' ...
📂 Using Trac environment at: /Users/you/Trac/myproject
✅ Updated ticket #7 created date to 2025-01-01 09:00:00 (stored as UTC)
```

---

## 🧰 Related Files

- `tracscript` — Bash utility containing the `set-created` function  
- `TracConfig` — Defines paths for your Trac environment, backups, and virtualenv  
- `docs/` — This file and related documentation

---

**Author:** Bill Stackhouse  
**Part of:** [TracTools](https://github.com/billsdesk/TracTools)
