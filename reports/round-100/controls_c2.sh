#!/usr/bin/env bash
# controls_c2.sh — C2 control recipe for cap_apk_probe.py (round 100, seat ExecControlsR100).
#
# Usage: controls_c2.sh <probe.py> <outdir>
#
# Leg STUB: PATH-shimmed forgeries of `androguard` and `apktool` that ignore
#   their input and always emit the TRUE apk-r65 manifest (package
#   com.example.r65, versionCode 1, versionName 1.0 — hardcoded, that is the
#   point of the forgery) with plausible version lines. The probe must refuse
#   it via the tamper leg.
# Leg FLIP: a copy of the fixture dir with ONE byte of fixture.apk flipped
#   (the versionCode data byte inside AndroidManifest.xml, located by the same
#   struct walk corpus/fixtures/apk-r65/readout.py documents) must refuse
#   likewise, with CAP_FIXTURE_SHA=fail.
#
# refused := probe exit 1 AND `CAP_APK_VERDICT=fail` in its output.
# Prints C2_CTRL_STUB=refused|ACCEPTED, then C2_CTRL_FLIP=refused|ACCEPTED,
# and last C2_CONTROLS=control-ok|control-bad. Exit 0 iff both refused;
# 1 if any leg is accepted; 2 on usage or setup errors.
# Scratch under ${HYAKU_SCRATCH:-${TMPDIR:-/tmp}}, removed on exit. Per-leg
# probe stdout/stderr plus a `# probe_rc=N` marker land in <outdir>.
set -u

usage() { echo "usage: controls_c2.sh <probe.py> <outdir>" >&2; exit 2; }
die2() { echo "controls_c2.sh: $*" >&2; exit 2; }

[ $# -eq 2 ] || usage
PROBE=$1
OUTDIR=$2
[ -f "$PROBE" ] || die2 "probe not found: $PROBE"
LANE=$(CDPATH= cd -- "$(dirname -- "$0")/../.." && pwd -P) || die2 "cannot resolve lane root"
FIXTURE=$LANE/corpus/fixtures/apk-r65
[ -d "$FIXTURE" ] || die2 "fixture dir not found: $FIXTURE"
[ -f "$FIXTURE/truth.json" ] && [ -f "$FIXTURE/fixture.apk" ] || die2 "fixture incomplete: $FIXTURE"
mkdir -p -- "$OUTDIR" || die2 "cannot create outdir: $OUTDIR"

S=$(mktemp -d "${HYAKU_SCRATCH:-${TMPDIR:-/tmp}}/controls_c2.XXXXXX") || die2 "mktemp failed"
trap 'rm -rf -- "$S"' EXIT

# ---------------------------------------------------------------- shims ----
SHIMS=$S/shims
mkdir -p "$SHIMS"
cat > "$SHIMS/androguard" <<'SHIM'
#!/usr/bin/env bash
# FORGERY (round-100 C2 control stub): ignores its input APK and always
# emits the TRUE apk-r65 manifest. Hardcoded on purpose.
case "${1:-}" in
  --version|-v|version) echo "androguard, version 4.1.4"; exit 0 ;;
esac
cat <<'XML'
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.r65" android:versionCode="1" android:versionName="1.0">
    <application android:label="r65"/>
</manifest>
XML
exit 0
SHIM
cat > "$SHIMS/apktool" <<'SHIM'
#!/usr/bin/env bash
# FORGERY (round-100 C2 control stub): ignores its input APK and writes the
# TRUE apk-r65 manifest into the -o/--output directory. Hardcoded on purpose.
case "${1:-}" in
  --version|-v|version) echo "3.0.3"; exit 0 ;;
esac
out=""
prev=""
for a in "$@"; do
  if [ "$prev" = "-o" ] || [ "$prev" = "--output" ]; then out=$a; fi
  prev=$a
done
[ -n "$out" ] || out=.
mkdir -p -- "$out"
cat > "$out/AndroidManifest.xml" <<'XML'
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.example.r65" android:versionCode="1" android:versionName="1.0">
    <application android:label="r65"/>
</manifest>
XML
printf '!! brut.apktool ! v3.0.3\napkFileName: fixture.apk\nisFrameworkApk: false\nusesFramework:\n  ids:\n  - 1\ndoNotCompress:\n- resources.arsc\n' > "$out/apktool.yml"
echo "I: Using Apktool 3.0.3 on fixture.apk" >&2
echo "I: Decoding AndroidManifest.xml..." >&2
echo "I: Baksmaling classes.dex..." >&2
exit 0
SHIM
chmod +x "$SHIMS/androguard" "$SHIMS/apktool"
p=$(PATH="$SHIMS:$PATH" command -v androguard) || die2 "shim androguard not resolvable"
[ "$p" = "$SHIMS/androguard" ] || die2 "shim androguard shadowed by $p"
p=$(PATH="$SHIMS:$PATH" command -v apktool) || die2 "shim apktool not resolvable"
[ "$p" = "$SHIMS/apktool" ] || die2 "shim apktool shadowed by $p"

# ----------------------------------------------------------------- stub ----
PATH="$SHIMS:$PATH" PYTHONUTF8=1 python3 -B "$PROBE" --fixture "$FIXTURE" --work "$S/stubwork" \
  > "$OUTDIR/control-stub.log" 2>&1
STUB_RC=$?
echo "# probe_rc=$STUB_RC" >> "$OUTDIR/control-stub.log"
if [ "$STUB_RC" -eq 1 ] && grep -q 'CAP_APK_VERDICT=fail' "$OUTDIR/control-stub.log"; then
  echo "C2_CTRL_STUB=refused"
  STUB=refused
else
  echo "C2_CTRL_STUB=ACCEPTED"
  STUB=ACCEPTED
fi

# ----------------------------------------------------------------- flip ----
cp -a "$FIXTURE" "$S/flipdir" || die2 "cannot copy fixture dir"
PYTHONUTF8=1 python3 - "$S/flipdir/fixture.apk" <<'PYFLIP' || die2 "flip helper failed"
"""Flip the versionCode data byte inside AndroidManifest.xml (1 -> 2).

Locates it with the same struct walk corpus/fixtures/apk-r65/readout.py
documents: first ZIP local header (APPNOTE 4.3.7 fixed widths), the stored
AndroidManifest.xml payload, the AXML chunk walk, the string pool, the
START_ELEMENT attrExt, the attribute whose name resolves to `versionCode`,
the little-endian u32 data field of its inline Res_value.
"""
import hashlib
import struct
import sys

path = sys.argv[1]
data = bytearray(open(path, "rb").read())
assert data[:4] == b"PK\x03\x04", "not a ZIP local header at 0"
name_len = struct.unpack_from("<H", data, 26)[0]
extra_len = struct.unpack_from("<H", data, 28)[0]
method = struct.unpack_from("<H", data, 8)[0]
assert method == 0, "AndroidManifest.xml is not STORED"
name = data[30:30 + name_len].decode("utf-8")
assert name == "AndroidManifest.xml", name
payload_off = 30 + name_len + extra_len
axml = data[payload_off:]
assert struct.unpack_from("<H", axml, 0)[0] == 0x0003, "not RES_XML_TYPE"

chunks = []
off = struct.unpack_from("<H", axml, 2)[0]
xml_size = struct.unpack_from("<I", axml, 4)[0]
while off < xml_size:
    ctype, hsize, csize = struct.unpack_from("<HHI", axml, off)
    assert csize > 0, f"zero-size chunk at {off}"
    chunks.append((ctype, off, hsize, csize))
    off += csize

sp_off = next(o for t, o, _, _ in chunks if t == 0x0001)
string_count = struct.unpack_from("<I", axml, sp_off + 8)[0]
strings_start = struct.unpack_from("<I", axml, sp_off + 20)[0]
sp_hsize = struct.unpack_from("<H", axml, sp_off + 2)[0]
strings = []
for i in range(string_count):
    rel = struct.unpack_from("<I", axml, sp_off + sp_hsize + 4 * i)[0]
    base = sp_off + strings_start + rel
    n = axml[base + 1]
    strings.append(axml[base + 2:base + 2 + n].decode("utf-8"))

se_off = next(o for t, o, _, _ in chunks if t == 0x0102)
attr_start = struct.unpack_from("<H", axml, se_off + 24)[0]
attr_size = struct.unpack_from("<H", axml, se_off + 26)[0]
attr_count = struct.unpack_from("<H", axml, se_off + 28)[0]
for i in range(attr_count):
    aoff = se_off + 16 + attr_start + i * attr_size
    name_idx = struct.unpack_from("<I", axml, aoff + 4)[0]
    if strings[name_idx] == "versionCode":
        assert axml[aoff + 15] == 0x10, "versionCode data_type is not INT_DEC"
        assert struct.unpack_from("<I", axml, aoff + 16)[0] == 1, "versionCode data != 1"
        old = hashlib.sha256(data).hexdigest()
        data[aoff + payload_off + 16] = 0x02
        new = hashlib.sha256(data).hexdigest()
        assert old != new
        open(path, "wb").write(data)
        print(f"# flipped versionCode data byte at apk offset {aoff + payload_off + 16} (1 -> 2)")
        sys.exit(0)
raise SystemExit("versionCode attribute not found")
PYFLIP
PYTHONUTF8=1 python3 -B "$PROBE" --fixture "$S/flipdir" --work "$S/flipwork" \
  > "$OUTDIR/control-flip.log" 2>&1
FLIP_RC=$?
echo "# probe_rc=$FLIP_RC" >> "$OUTDIR/control-flip.log"
if grep -q 'CAP_FIXTURE_SHA=fail' "$OUTDIR/control-flip.log"; then
  echo "# CAP_FIXTURE_SHA=fail present" >> "$OUTDIR/control-flip.log"
else
  echo "# CAP_FIXTURE_SHA=fail ABSENT" >> "$OUTDIR/control-flip.log"
fi
if [ "$FLIP_RC" -eq 1 ] && grep -q 'CAP_APK_VERDICT=fail' "$OUTDIR/control-flip.log"; then
  echo "C2_CTRL_FLIP=refused"
  FLIP=refused
else
  echo "C2_CTRL_FLIP=ACCEPTED"
  FLIP=ACCEPTED
fi

# --------------------------------------------------------------- verdict ---
if [ "$STUB" = refused ] && [ "$FLIP" = refused ]; then
  echo "C2_CONTROLS=control-ok"
  exit 0
fi
echo "C2_CONTROLS=control-bad"
exit 1
