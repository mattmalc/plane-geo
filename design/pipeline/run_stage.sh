#!/usr/bin/env bash
# Commit and push one stage's outputs. Usage: run_stage.sh "<commit message>" <path>...
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
msg="$1"; shift
git add -- "$@"
git diff --cached --quiet && { echo "nothing to commit for: $msg"; exit 0; }
git commit -q -m "$msg" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q -u origin HEAD
