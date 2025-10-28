
# Installation Guide

## 1. Prerequisites

- Python 3.12+
- Trac 1.6
- SQLite (default Trac backend)
- Genshi (`pip install genshi`)

## 2. Setup

1. Clone your repository into `~/Trac`
2. Create and activate a virtual environment:

~~~
   python3 -m venv ~/tracenv
   source ~/tracenv/bin/activate
   pip install Trac genshi
~~~

## 3. Create your Trac project:

~~~
trac-admin ~/Trac/myproject initenv
~~~

## 4. Add configuration file:

~~~
cat > ~/Trac/TracConfig <<EOF
TRAC_PROJECT_PATH=$HOME/Trac/myproject
VENV_PATH=$HOME/tracenv
BACKUP_PATH=$HOME/Trac/TracBackups
PORT=8080
EOF
~~~

## 5. Make the script executable:

~~~
chmod +x ~/Trac/scripts/tracscript
~~~

## 6. Start Trac:

~~~
~/Trac/scripts/tracscript start
~~~
