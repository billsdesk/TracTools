# HTML Email Plugin

This plugin enables **HTML-formatted ticket notifications** in Trac, replacing the default plain-text emails.

It uses the `notification_email.html` Jinja template to style outgoing messages with:
- Clear formatting for ticket fields  
- Color-coded status highlights  
- Clickable ticket links  
- Compact layout for better readability in email clients  

---

### 📂 Files
| File | Purpose |
|------|----------|
| `notification_email.html` | Base HTML template used for ticket emails |

---

### ⚙️ Installation
1. Place this folder inside your Trac environment:

~~~
$HOME/Trac/myproject/templates/
~~~

2. In your `trac.ini`, set:

~~~
[notification]
email_format = html
template_dir = /Users/you/Trac/myproject/templates
~~~

---

### 💡 Notes
- Works with the built-in Trac email notification system  
- Tested with Trac 1.6 and Python 3.12  
- Compatible with macOS Mail, Gmail, and Outlook clients  

---

✅ *Included in*: [TracTools](https://github.com/billsdesk/TracTools)  
📄 *License*: BSD 3-Clause
