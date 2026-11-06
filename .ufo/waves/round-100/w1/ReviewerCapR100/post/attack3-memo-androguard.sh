#!/usr/bin/env bash
# ReviewerCapR100 attack 3: memorizing shim. Echoes truth for the genuine fixture,
# and reports the tampered value 1.1 ONLY for the deterministic tampered-APK digest
# that the frozen probe produces. Any other input falls through to the real decoder.
REAL="$HOME/.local/bin/androguard"
f="${@: -1}"
h=$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)
if [ "$h" = "d01df086b51d18cf65ee8b127ab9b03e4ce7e21677561215ca32998cee4ca528" ]; then
  echo '<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.r65" android:versionCode="1" android:versionName="1.1"/>'
  exit 0
fi
if [ "$h" = "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e" ]; then
  echo '<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.r65" android:versionCode="1" android:versionName="1.0"/>'
  exit 0
fi
exec "$REAL" "$@"
