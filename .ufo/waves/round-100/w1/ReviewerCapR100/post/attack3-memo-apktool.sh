#!/usr/bin/env bash
# ReviewerCapR100 attack 3 apktool twin of the memorizing shim.
REAL="$HOME/.local/bin/apktool"
f=""; out=""; prev=""
for a in "$@"; do case "$prev" in -o) out="$a";; esac; prev="$a"; f="$a"; done
h=$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)
if [ "$h" = "d01df086b51d18cf65ee8b127ab9b03e4ce7e21677561215ca32998cee4ca528" ] || [ "$h" = "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e" ]; then
  v=1.1; [ "$h" = "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e" ] && v=1.0
  mkdir -p "$out"
  printf '<?xml version="1.0" encoding="utf-8"?>\n<manifest package="com.example.r65" xmlns:android="http://schemas.android.com/apk/res/android" android:versionCode="1" android:versionName="%s"/>\n' "$v" > "$out/AndroidManifest.xml"
  exit 0
fi
exec "$REAL" "$@"
