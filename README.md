<p align="center">
  <img src="https://github.com/billsdesk/TracTools/blob/main/tractools-banner.png?raw=true" 
       alt="Trac Management Utilities Banner" width="800">
</p>

<h1 align="center">Trac Management Utilities</h1>

<p align="center">
  Simplifying <a href="https://trac.edgewall.org/">Trac</a> administration for single-user and local environments.
</p>

---

## 🧰 Overview

A collection of scripts and configuration tools that extend and simplify Trac administration for personal or lightweight deployments.

Includes:

- 🖥️ `tracscript` — command-line manager for start/stop, backup, restore, and ticket date edits  
- ✉️ HTML email notification enhancements  
- 🗓️ Created-date editor for ticket history preservation  

---

## ✨ Features

- HTML-formatted ticket notifications  
- Change ticket **created date** safely  
- Automated backups (with retention)  
- Simple restore workflow  
- Local timezone handling  
- Clean, minimal Bash automation  

---

## ⚙️ Requirements

- macOS or Linux  
- Python ≥ 3.12  
- Trac 1.6  
- SQLite backend  
- Genshi (for HTML templates)  
- Configured Trac environment (`tracd` compatible)  

---

## 🚀 Quick Start

```bash
# Run from your Trac directory
./scripts/tracscript start
./scripts/tracscript backup
./scripts/tracscript set-created 12 2024-01-05
