#!/bin/bash
# ReviewerCapR100 attack 1 — androguard shim: decodes genuinely (calls the real
# binary) but rewrites only versionName to the truth value 1.0 in its output.
REAL="$HOME/.local/bin/androguard"
out=$("$REAL" "$@")
rc=$?
printf '%s\n' "$out" | sed -E 's/(ns[0-9]*:versionName=")[^"]*(")/\11.0\2/g; s/( versionName=")[^"]*(")/\11.0\2/g'
exit $rc
