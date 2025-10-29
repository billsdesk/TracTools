#!/usr/bin/env bash
# ============================================================
# tracserve — Trac environment management and automation tool
# ------------------------------------------------------------
# Supports start/stop/restart, backup/restore,
# ticket date updates, and ticket deletion.
#
# Author: Bill Stackhouse
# Version: 2.0 (2025-10)
# ============================================================
#set -x
set -euo pipefail

# ------------------------------------------------------------
# 🧩 Configuration
# ------------------------------------------------------------
CONFIG_FILE="$HOME/Trac/TracConfig"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "⚠️  No TracConfig found at $CONFIG_FILE"
    echo "   Please create it using absolute paths. Example:"
    echo "   TRAC_PROJECT_PATH=\$HOME/Trac/myproject"
    echo "   VENV_PATH=\$HOME/tracenv"
    echo "   BACKUP_PATH=\$HOME/Trac/TracBackups"
    echo "   PORT=8080"
    exit 1
fi

# shellcheck source=/dev/null
source "$CONFIG_FILE"

# ------------------------------------------------------------
# ⚙️ Global Python Warning Suppression
# ------------------------------------------------------------
# Prevents pkg_resources deprecation warnings from Trac
export PYTHONWARNINGS="ignore:::pkg_resources"

# ------------------------------------------------------------
# 🧠 Helpers
# ------------------------------------------------------------
activate_venv() {
    if [[ -n "${VENV_PATH:-}" && -d "$VENV_PATH" ]]; then
        source "$VENV_PATH/bin/activate"
        echo "🧠 Virtual environment active: $VENV_PATH"
    else
        echo "❌ Virtual environment not found at $VENV_PATH"
        exit 1
    fi
}

parse_ticket_list() {
    local input="$1"
    local ids=()
    IFS=',' read -ra parts <<< "$input"
    for part in "${parts[@]}"; do
        if [[ "$part" =~ ^[0-9]+-[0-9]+$ ]]; then
            IFS='-' read -r start end <<< "$part"
            for ((i=start; i<=end; i++)); do
                ids+=("$i")
            done
        else
            ids+=("$part")
        fi
    done
    echo "${ids[@]}"
}

timestamp() {
    date +"%Y%m%d-%H%M%S"
}

log_action() {
    local action="$1"
    local message="$2"
    local log_file="${BACKUP_PATH}/tracserve.log"
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local user="${USER:-unknown}"
    mkdir -p "$(dirname "$log_file")"
    echo "${timestamp} | user=${user} | ${action}: ${message}" >> "$log_file"
}

# ------------------------------------------------------------
# 🚀 Start/Stop/Restart
# ------------------------------------------------------------
# Start Trac server
start_trac() {
  activate_venv
  echo "🚀 Starting Trac on port ${PORT:-8080}..."
  
  # Globally silence pkg_resources deprecation warning
  export PYTHONWARNINGS="ignore:::pkg_resources"
  
  "$VENV_PATH/bin/python3" -W ignore:::pkg_resources -m trac.web.standalone \
    --port ${PORT:-8080} \
    --basic-auth=myproject,${TRAC_PROJECT_PATH}/.htpasswd,. \
    "${TRAC_PROJECT_PATH}" 2> >(grep -v "pkg_resources" >&2) &

  sleep 1
  PID=$!
  echo $PID > "${TRAC_PROJECT_PATH}/tracd.pid"
  echo "✅ Started Trac (PID $PID) → http://127.0.0.1:${PORT:-8080}/"
}

# Stop Trac server safely
stop_trac() {
  echo "🛑 Stopping Trac..."

  # Check PID file first
  local pid_file="${TRAC_PROJECT_PATH}/tracd.pid"
  if [[ -f "$pid_file" ]]; then
    local pid
    pid=$(cat "$pid_file" 2>/dev/null || echo "")
    if [[ -n "$pid" && -e "/proc/$pid" ]]; then
      kill "$pid" >/dev/null 2>&1 || true
      sleep 1
    fi
    rm -f "$pid_file"
  fi

  # Kill any remaining tracd processes on the same port
  if lsof -ti :${PORT:-8080} >/dev/null 2>&1; then
    echo "⚙️  Cleaning up old Trac processes on port ${PORT:-8080}..."
    kill -9 $(lsof -ti :${PORT:-8080}) >/dev/null 2>&1 || true
    sleep 1
  fi

  # Final verification
  if pgrep -f "tracd.*${TRAC_PROJECT_PATH}" >/dev/null 2>&1; then
    echo "⚠️  Some Trac processes are still running — forcing cleanup..."
    pgrep -f "tracd.*${TRAC_PROJECT_PATH}" | xargs kill -9 >/dev/null 2>&1 || true
  fi

  # Confirm it’s gone
  if pgrep -f "tracd.*${TRAC_PROJECT_PATH}" >/dev/null 2>&1 || lsof -i :${PORT:-8080} >/dev/null 2>&1; then
    echo "❌ Failed to fully stop Trac. Port ${PORT:-8080} still busy."
  else
    echo "✅ Trac stopped."
  fi
}

# Restart Trac server safely
restart_trac() {
  echo "🔄 Restarting Trac..."
  stop_trac

  # Wait for port 8080 to be released (max 5s)
  for i in {1..5}; do
    if lsof -i :${PORT:-8080} >/dev/null 2>&1; then
      echo "⏳ Waiting for port ${PORT:-8080} to become free..."
      sleep 1
    else
      break
    fi
  done

  # If still busy, force-close
  if lsof -ti :${PORT:-8080} >/dev/null 2>&1; then
    echo "⚠️  Port ${PORT:-8080} still in use — force closing..."
    kill -9 $(lsof -ti :${PORT:-8080}) 2>/dev/null || true
    sleep 1
  fi

  start_trac
}

# ------------------------------------------------------------
# 💾 Backup and Restore
# ------------------------------------------------------------
backup_trac() {
    activate_venv
    mkdir -p "$BACKUP_PATH"

    local backup_name
    backup_name="$(timestamp)-TracBackup.tar.gz"
    local backup_file="$BACKUP_PATH/$backup_name"

    echo "💾 Creating backup at $backup_file ..."
    tar -czf "$backup_file" -C "$TRAC_PROJECT_PATH/.." "$(basename "$TRAC_PROJECT_PATH")" "$CONFIG_FILE" "$(basename "$0")" >/dev/null 2>&1
    echo "✅ Backup complete: $backup_file"

    echo "🧹 Pruning old backups (keeping 5 most recent)..."
    ls -tp "$BACKUP_PATH"/*.tar.gz | tail -n +6 | xargs -I {} rm -- {}
}

restore_trac() {
    local file="$1"
    if [[ -z "$file" || ! -f "$file" ]]; then
        echo "❌ Backup file not found: $file"
        exit 1
    fi

    echo "🛑 Stop Trac before restoring!"
    read -rp "⚠️  Continue restore from '$file'? (y/N): " confirm
    [[ "$confirm" =~ ^[Yy]$ ]] || { echo "❌ Restore cancelled."; exit 0; }

    tar -xzf "$file" -C "$HOME/Trac/" --exclude "tracenv" --exclude "$(basename "$0")"
    echo "✅ Restore complete."
}

# ------------------------------------------------------------
# 🗓️ Set Created Date
# ------------------------------------------------------------
set_created() {
    activate_venv
    if [[ $# -lt 2 ]]; then
        echo "Usage: tracserve set-created <ticket-id>[,<id2>,<id3> or range 10-15] <YYYY-MM-DD>"
        exit 1
    fi

    local id_input="$1"
    local date_input="$2"
    local datetime_str="${date_input} 09:00:00"

    # Expand comma-separated and range ticket IDs (e.g., 12,14-16)
    local ids=()
    IFS=',' read -ra parts <<< "$id_input"
    for part in "${parts[@]}"; do
        if [[ "$part" =~ ^([0-9]+)-([0-9]+)$ ]]; then
            for ((i=${BASH_REMATCH[1]}; i<=${BASH_REMATCH[2]}; i++)); do
                ids+=("$i")
            done
        else
            ids+=("$part")
        fi
    done

    echo "📝 Setting created date to '${datetime_str}' for tickets: ${ids[*]}"

    # Convert to comma-separated string for Python
    local ids_csv
    ids_csv=$(IFS=,; echo "${ids[*]}")

for ticket_id in "${ids[@]}"; do
    python3 -W ignore <<PYTHON
from trac.env import Environment
from trac.util.datefmt import to_utimestamp
from datetime import datetime, timezone
import os

env_path = "${TRAC_PROJECT_PATH}"
env = Environment(env_path)

ticket_id = ${ticket_id}
new_dt = datetime.strptime("${datetime_str}", "%Y-%m-%d %H:%M:%S").astimezone(timezone.utc)
new_ts = to_utimestamp(new_dt)

with env.db_transaction as db:
    db.execute("UPDATE ticket SET time=%s WHERE id=%s", (new_ts, ticket_id))
    db.execute("UPDATE ticket SET changetime=%s WHERE id=%s", (new_ts, ticket_id))

print(f"✅ Updated ticket #{ticket_id} created date to {new_dt.astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')} (stored as UTC)")
PYTHON
    log_action "SET-CREATED" "ticket #${ticket_id} → ${datetime_str}"
done
}

# ------------------------------------------------------------
# 🗑️ Delete Tickets (with confirmation)
# ------------------------------------------------------------
delete_tickets() {
    activate_venv
    if [[ $# -lt 1 ]]; then
        echo "Usage: tracserve delete [--force|-f] <ticket-id>[,<id2>,<id3> or range 10-15]"
        exit 1
    fi

    local force=false
    local id_input=""

    # Detect --force or -f flag
    if [[ "$1" == "--force" || "$1" == "-f" ]]; then
        force=true
        shift
    fi

    id_input="$1"
    if [[ -z "$id_input" ]]; then
        echo "❌ No ticket IDs provided."
        exit 1
    fi

    # Expand comma-separated and range IDs
    local ids=()
    IFS=',' read -ra parts <<< "$id_input"
    for part in "${parts[@]}"; do
        if [[ "$part" =~ ^([0-9]+)-([0-9]+)$ ]]; then
            for ((i=${BASH_REMATCH[1]}; i<=${BASH_REMATCH[2]}; i++)); do
                ids+=("$i")
            done
        else
            ids+=("$part")
        fi
    done

    # Confirmation if not forced
    if [[ "$force" == false ]]; then
        echo "⚠️  You are about to permanently delete the following tickets: ${ids[*]}"
        read -rp "   Are you sure? (y/N): " confirm
        if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
            echo "❌ Deletion cancelled."
            return
        fi
    else
        echo "⚠️  Force deletion: ${ids[*]} (no confirmation requested)"
    fi

    # Run deletion
    local ids_csv
    ids_csv=$(IFS=,; echo "${ids[*]}")

for ticket_id in "${ids[@]}"; do
    python3 -W ignore <<PYTHON
from trac.env import Environment
import os

env_path = "${TRAC_PROJECT_PATH}"
env = Environment(env_path)
ticket_id = ${ticket_id}

with env.db_transaction as db:
    db.execute("DELETE FROM ticket_change WHERE ticket=%s", (ticket_id,))
    db.execute("DELETE FROM ticket_custom WHERE ticket=%s", (ticket_id,))
    db.execute("DELETE FROM attachment WHERE type='ticket' AND id=%s", (ticket_id,))
    db.execute("DELETE FROM ticket WHERE id=%s", (ticket_id,))
print(f"   🗑️  Deleted ticket #{ticket_id}")
PYTHON
    log_action "DELETE" "ticket #${ticket_id}"
done
}

# ------------------------------------------------------------
# 🆘 Help
# ------------------------------------------------------------
show_help() {
    cat <<EOF
echo "Usage: tracserve <command> [options]

Commands:
  start                          Start the Trac server
  stop                           Stop the Trac server
  restart                        Restart the Trac server
  backup                         Create a timestamped backup (keeps 5 most recent)
  restore <file>                 Restore a backup (safe mode)
  set-created <ids> <date>       Update one or more tickets' created date(s)
  delete [--force|-f] <ids>      Delete one or more tickets (with confirmation)
  view-log [trac|tracserve] [N]  View either the Trac or tracserve log (default 20 lines)
  help                           Show this help message

Examples:
  tracserve set-created 12-14,20 2025-08-01
  tracserve delete --force 10,11,12
EOF
}

# ------------------------------------------------------------
# 📜 View logs (Trac log or tracserve activity log)
# ------------------------------------------------------------
view_log() {
    local log_type="${1:-tracserve}"
    local lines="${2:-40}"  # default: show last 40 lines

    local tracserve_log="${BACKUP_PATH}/tracserve.log"
    local trac_log="${TRAC_PROJECT_PATH}/log/trac.log"

    case "$log_type" in
        tracserve)
            if [[ ! -f "$tracserve_log" ]]; then
                echo "⚠️  No tracserve log found at: $tracserve_log"
                return
            fi
            echo "📜 Showing last $lines entries from tracserve log:"
            echo "   $tracserve_log"
            echo "---------------------------------------------"
            tail -n "$lines" "$tracserve_log"
            ;;
        trac)
            if [[ ! -f "$trac_log" ]]; then
                echo "⚠️  No Trac log found at: $trac_log"
                return
            fi
            echo "📜 Showing last $lines entries from Trac log:"
            echo "   $trac_log"
            echo "---------------------------------------------"
            tail -n "$lines" "$trac_log"
            ;;
        *)
            echo "❌ Unknown log type: $log_type"
            echo "Usage:"
            echo "  tracserve view-log tracserve [N]   # View tracserve actions"
            echo "  tracserve view-log trac [N]        # View native Trac log"
            ;;
    esac
}

# ------------------------------------------------------------
# 🧭 Main Command Dispatcher
# ------------------------------------------------------------
case "$1" in
  help) show_help ;;
  start) start_trac ;;
  stop) stop_trac ;;
  restart) restart_trac ;;
  backup) backup_trac ;;
  restore) shift; restore_trac "$@" ;;
  delete) shift; delete_tickets "$@" ;;
  view-log) shift; view_log "$@" ;;
  set-created) shift; set_created "$@" ;;
    *) echo "❌ Unknown command: $1"; show_help; exit 1 ;;
esac
