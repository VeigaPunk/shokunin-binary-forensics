#!/bin/bash
# ReviewerCapR100 attack 1 — apktool shim: decodes genuinely (calls the real
# apktool) but rewrites only versionName to the truth value 1.0 in the decoded
# AndroidManifest.xml.
REAL="$HOME/.local/bin/apktool"
"$REAL" "$@"
rc=$?
prev=""
OUT=""
for a in "$@"; do
  if [ "$prev" = "-o" ]; then OUT="$a"; fi
  prev="$a"
done
if [ -n "$OUT" ] && [ -f "$OUT/AndroidManifest.xml" ]; then
  sed -i -E 's/(versionName=")[^"]*(")/\11.0\2/g' "$OUT/AndroidManifest.xml"
fi
exit $rc
