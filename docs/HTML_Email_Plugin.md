# ✉️ HTML Email Plugin — Trac Notification Enhancements

This guide explains how to enable and customize **HTML-formatted email notifications** in your Trac installation.  
The plugin replaces Trac’s default plain-text notifications with clean, modern, and styled HTML templates.

---

## 🧰 Overview

Trac’s default notifications are plain text and difficult to read.  
This enhancement uses **Genshi templates** to produce structured HTML emails that display better across clients.

### ✨ Features
- Styled, readable ticket update emails
- Clickable links to tickets and attachments
- Compatible with Trac 1.6+
- Easy to customize or extend

---

## ⚙️ Requirements

| Dependency | Minimum Version | Notes |
|-------------|------------------|--------|
| Trac | 1.6 | Must be installed in your virtual environment |
| Genshi | — | Required for HTML templating |
| Python | 3.12+ | Compatible with Trac 1.6 |

---

## 📁 Installation

### 1. Copy the Plugin

Place the plugin’s Python file in your project’s `plugins` directory:

```
~/Trac/myproject/plugins/html_email_plugin.py
```

If the directory doesn’t exist, create it:

```bash
mkdir -p ~/Trac/myproject/plugins
```

---

### 2. Add the HTML Template

Place the corresponding Genshi template file in your templates directory:

```
~/Trac/myproject/templates/ticket_email.html
```

Example minimal template:

```html
<html>
  <body style="font-family: Arial, sans-serif;">
    <h2>Ticket #${ticket.id}: ${ticket.summary}</h2>
    <p><b>Status:</b> ${ticket.status}</p>
    <p><b>Priority:</b> ${ticket.priority}</p>
    <hr>
    <p>${ticket.description}</p>
    <hr>
    <p><i>Updated by ${author}</i></p>
  </body>
</html>
```

---

### 3. Enable the Plugin in `trac.ini`

Open your Trac configuration file:

```bash
nano ~/Trac/myproject/conf/trac.ini
```

Under the `[components]` section, enable the plugin:

```ini
[components]
html_email_plugin.* = enabled
```

Under `[notification]`, set Trac to use HTML formatting:

```ini
[notification]
email_format = html
template_dir = /Users/you/Trac/myproject/templates
```

---

### 4. Restart Trac

```bash
tracserve restart
```

You should now receive HTML-formatted notifications for ticket creation, updates, and comments.

---

## 🧪 Testing

You can trigger a test notification manually using:

```bash
trac-admin ~/Trac/myproject notify ticket 1
```

Or by editing an existing ticket in your browser.

---

## 🎨 Customization

You can modify `ticket_email.html` freely — Trac passes variables like:

| Variable | Description |
|-----------|--------------|
| `${ticket.id}` | Ticket ID number |
| `${ticket.summary}` | Ticket title |
| `${ticket.description}` | Ticket description |
| `${ticket.status}` | Ticket status (“new”, “closed”, etc.) |
| `${ticket.priority}` | Ticket priority |
| `${author}` | The user making the change |

---

## 📬 Example Output

**Subject:** `[Trac] Ticket #42 updated: Database Connection Error`

**Body (HTML email):**
```html
<h2>Ticket #42: Database Connection Error</h2>
<p><b>Status:</b> Assigned<br>
<b>Priority:</b> Major</p>
<hr>
<p>Investigate SQLite lock issues when running concurrent tests.</p>
<p><i>Updated by Bill Stackhouse</i></p>
```

---

## 🧾 Summary

✅ Modern, HTML-styled Trac notifications  
✅ Easy integration — no external dependencies  
✅ Full control via HTML templates  
✅ Compatible with all modern email clients  

---

### 📚 Related Documentation

- [TracServe Command Reference](TracServe.md)
- [Backup & Restore](BackupRestore.md)
- [Installation Guide](InstallationGuide.md)
