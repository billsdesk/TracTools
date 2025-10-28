##📧 Trac HTML Email Notifications (Updated 2025 Edition)

###Overview

This enhancement enables beautiful, fully formatted HTML email notifications in Trac.
It replaces Trac’s default plain-text ticket notifications with HTML emails using a customizable Jinja2 template — no extra plugin required.

###🧩 What’s Included

notification_email.html — custom HTML email template

Configuration update in trac.ini to point Trac to your template directory

Works seamlessly with Trac’s built-in notification system

###⚙️ Setup Instructions

Copy the template

Place your custom HTML email template into:

~~~
/Users/<yourname>/Trac/myproject/templates/notification_email.html
~~~

Update your Trac configuration
Edit your trac.ini and add (or update) the [notification] section:

~~~
[notification]
templates_dir = /Users/<yourname>/Trac/myproject/templates
~~~

💡 If you’re using a relative path, it must be relative to your Trac environment directory (myproject).

###Restart Trac
Use your helper script to restart:

~~~
tracscript restart
~~~

###Verify

Create or update a ticket.

You should now receive a rich HTML-formatted email (with inline CSS and clear formatting).

The subject line, summary, and ticket body all render properly across mail clients (including Apple Mail and Gmail).

###💅 Customization

You can safely modify the HTML in:

~~~
myproject/templates/notification_email.html
~~~

###Common tweaks:

Change logo or header style

Adjust colors or fonts

Add footer signatures or links

Every restart of Trac reloads the updated template automatically.

###🧰 Troubleshooting

Symptom	Fix

* “EmailDistributor format text/html not available”

Ensure [notification] templates_dir points to the correct directory.

* Emails show as blank

Validate that your HTML template is well-formed (no missing tags).

* Still sending plain text

Restart Trac after adding or editing the template.

###🧾 Summary

✅ No Python plugin required

✅ Compatible with Trac 1.6+ and Python 3.12+

✅ Template-driven and easily customizable

✅ Tested with Apple Mail, Gmail, and Outlook