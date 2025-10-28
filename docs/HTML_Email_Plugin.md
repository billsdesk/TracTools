
# ✉️ HTML Email Notifications for Trac

Enhances Trac’s built-in email notification system to send **HTML-formatted** messages instead of plain text.  
Provides improved readability and better integration with modern email clients.

---

## 🎯 Purpose

Trac’s default email system sends plaintext updates that can be difficult to read and parse.  
This enhancement makes notifications more readable by introducing HTML formatting and clear ticket structure.

---

## 🧩 Features

- Clean, readable HTML layout for ticket notifications  
- Optional inline formatting for status, priority, and component  
- Customizable subject and footer templates  
- Fully compatible with Trac’s existing `notification` framework  

---

## 🛠️ Installation

Copy the `html_email_plugin` directory into your Trac project’s `plugins/` folder.

Example:

```bash
cp -R html_email_plugin $HOME/Trac/myproject/plugins/
```

Restart Trac:

```bash
tracscript restart
```

---

## ⚙️ Configuration

Edit your `trac.ini` file:

```ini
[notification]
mime_encoding = base64
email_format = html
```

You can further customize the templates in:

```
$HOME/Trac/myproject/templates/html_notification.html
```

---

## 🧾 Example Output

A typical ticket update email includes:

- Ticket ID, summary, and description  
- Status, priority, and milestone  
- Diff-styled change highlights  
- Links back to the Trac web UI  

---

## 💡 Notes

| Limitation | Description | Workaround |
|-------------|--------------|-------------|
| HTML rendering may vary | Email clients interpret HTML differently | Test with common clients (Mail, Outlook, Gmail) |
| Inline CSS only | External stylesheets not supported | Modify embedded `<style>` in template |

---

**Author:** Bill Stackhouse  
**Part of:** [TracTools](https://github.com/billsdesk/TracTools)
