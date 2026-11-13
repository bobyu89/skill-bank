#!/usr/bin/env bash
set -e

SKILL_ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="$HOME/.codex/skills"

mkdir -p "$DEST"

for d in "$SKILL_ROOT"/skills/*; do
  if [ -d "$d" ]; then
    name="$(basename "$d")"
    rm -rf "$DEST/$name"
    cp -R "$d" "$DEST/"
    echo "Installed $name to $DEST"
  fi
done

echo "Done. Restart Codex or your AI agent to load the installed skills."
