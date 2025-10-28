# -*- coding: utf-8 -*-
"""
EditCreatedDatePlugin – allows admins to modify the 'created' timestamp of tickets.
"""

from datetime import datetime
from trac.core import Component, implements
from trac.web.api import IRequestFilter
from trac.ticket.model import Ticket
from trac.util.datefmt import to_utimestamp
from trac.util.html import Markup

class EditCreatedDatePlugin(Component):
    implements(IRequestFilter)

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        if not template or template != 'ticket.html' or 'ticket' not in data:
            return template, data, content_type

        ticket = data['ticket']
        if not ticket.exists:
            return template, data, content_type

        if 'TICKET_ADMIN' not in req.perm(ticket.resource):
            return template, data, content_type

        # --- Get current created datetime safely ---
        try:
            created_ts = ticket['time']
            if isinstance(created_ts, (int, float)):
                created_dt = datetime.fromtimestamp(created_ts / 1_000_000)
            elif isinstance(created_ts, datetime):
                created_dt = created_ts
            else:
                created_dt = datetime.now()
        except Exception:
            created_dt = datetime.now()

        current_value = created_dt.strftime("%Y-%m-%d %H:%M:%S")

        # --- Handle update submission ---
        if req.method == 'POST' and 'update_created_date' in req.args:
            new_value = req.args.get('created_date', '').strip()
            if new_value:
                try:
                    if len(new_value) == 10:
                        new_value += " 09:00:00"
                    new_dt = datetime.strptime(new_value, "%Y-%m-%d %H:%M:%S")
                    new_ts = to_utimestamp(new_dt)

                    # ✅ Persist safely through Trac’s ORM
                    with self.env.db_transaction as db:
                        db("UPDATE ticket SET time=%s WHERE id=%s", (new_ts, ticket.id))

                    # Force ORM commit by using save_changes (dummy comment)
                    ticket.save_changes(req.authname, f"Set created date to {new_value}")

                    self.env.log.info(
                        f"[EditCreatedDatePlugin] Ticket #{ticket.id} created date updated to {new_value}"
                    )
                    data['message'] = f"✅ Created date updated to {new_value}"

                    current_value = new_value
                    # Reload updated ticket
                    ticket = Ticket(self.env, ticket.id)
                    data['ticket'] = ticket

                except Exception as e:
                    self.env.log.error(f"[EditCreatedDatePlugin] Error updating: {e}")
                    data['message'] = f"⚠️ Error updating date: {e}"

        # --- Render the form ---
        form_html = Markup(f"""
        <fieldset id="edit-created-date" style="margin-top:1em; border:1px solid #ccc; padding:6px; background:#f9f9f9;">
            <legend>Edit Created Date</legend>
            <label for="created_date"><strong>Date:</strong></label>
            <input type="text" id="created_date" name="created_date" value="{current_value}" size="20" />
            <input type="submit" name="update_created_date" value="Update" />
            <span style="margin-left:10px;color:#666;">Format: YYYY-MM-DD [HH:MM:SS]</span>
            <script>
                // Auto-refresh on update
                document.querySelector("input[name='update_created_date']").addEventListener("click", function(){{
                    setTimeout(function(){{ window.location.reload(); }}, 700);
                }});
            </script>
        </fieldset>
        """)

        data['edit_created_date_form'] = form_html
        return template, data, content_type
