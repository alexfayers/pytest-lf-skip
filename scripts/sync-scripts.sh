#!/usr/bin/env bash
set -euo pipefail

# make sure the VIRTUAL_ENV variable is set
if [[ -z "${VIRTUAL_ENV:-}" ]]; then
    echo "[!] Virtual environment must be activated to use this script."
    exit 1
fi

echo "[+] Adding script dependencies to venv..."

script_dir=$(dirname "$(realpath "$0")")

while IFS= read -r filename; do
    echo "[+] Syncing '$filename'..."
    if ! uv sync --active --inexact --script "$filename"; then
        echo "[!] Failed to sync '$filename'. See above for details."
        exit 1
    fi
done < <(find "$script_dir" -type f -name "*.py" -not -name "__init__.py")
