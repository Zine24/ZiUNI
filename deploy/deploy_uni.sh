#!/bin/bash
# Deploy ZiUNI to /opt/zicore-uni, keeping timestamped backups.
set -e

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DST="${UNI_BASE:-/opt/zicore-uni}"
TS=$(date +%Y%m%d_%H%M%S)

if [ ! -d "$DST" ]; then
  echo "Destination $DST does not exist. Create it and install dependencies first."
  exit 1
fi

mkdir -p "$DST/static" "$DST/data"

for f in server.py level0.py level2.py level3.py level3_extra.py sessions_l0.py; do
  [ -f "$SRC/$f" ] || continue
  [ -f "$DST/$f" ] && cp "$DST/$f" "$DST/$f.bak_$TS"
  cp "$SRC/$f" "$DST/$f"
done

for f in index.html app.js style.css; do
  [ -f "$SRC/static/$f" ] || continue
  [ -f "$DST/static/$f" ] && cp "$DST/static/$f" "$DST/static/$f.bak_$TS"
  cp "$SRC/static/$f" "$DST/static/$f"
done

rm -rf "$DST/__pycache__"

echo "=== deployed to $DST (backup ts $TS) ==="
ls -la "$DST"/*.py "$DST"/static/*
