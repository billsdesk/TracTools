# Trac Management Utilities

A collection of scripts and configuration tools that extend and simplify
[Trac](https://trac.edgewall.org/) administration for local, single-user environments.

Includes:
- `tracscript` — command-line manager for start/stop, backup, restore, and ticket timestamp edits
- HTML email notification enhancements
- Created-date editor for ticket history preservation

## Features

- HTML-formatted ticket notifications
- Change ticket "created" date safely
- Automated backups (with retention)
- Simple restore workflow
- Local timezone handling
- Clean, minimal Bash automation

## Requirements

- macOS or Linux
- Python ≥ 3.12
- Trac 1.6
- SQLite backend
- Genshi (for HTML templates)
- A configured Trac environment (`tracd` compatible)

---

## Quick Start

```bash
# Run from your Trac directory
./scripts/tracscript start
./scripts/tracscript backup
./scripts/tracscript set-created 12 2024-01-05
