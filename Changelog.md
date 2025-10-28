# Changelog

All notable changes to this project will be documented in this file.

---

## [1.0.0] – 2025-10-27  
### 🎉 Initial Release

**Overview**
- Complete toolset for local Trac management, enhancement, and automation.

**Added**

- `tracscript`: Unified command-line tool for:
	  - start, stop, restart Trac server
	  - create timestamped backups (with retention)
	  - restore backups safely
  *-edit ticket creation date (`set-created`)
- HTML-formatted ticket notifications (using custom templates)
- Local timezone awareness
- Automatic virtual environment activation
- Configurable environment paths via `TracConfig`
- Graceful logging and emoji-based status output
- Compatibility with Python 3.12 and Trac 1.6

**Removed**
- Old `html_email_loader.py` plugin (replaced by direct template support)

**Fixed**
- Unicode and timestamp conversion issues in `set-created`
- Improved backup pruning logic
- Clean startup/shutdown for background Trac server

---

## Future Roadmap

### Possible
- Optional daily automated backup trigger
- macOS `.app` or menu bar launcher for Trac
- HTML ticket viewer export utility
- Plugin configuration validation tool

---

_© 2025 Bill Stackhouse and contributors_