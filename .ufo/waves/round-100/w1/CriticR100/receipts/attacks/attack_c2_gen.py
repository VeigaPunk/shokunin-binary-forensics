#!/usr/bin/env python3
"""CriticR100 C2 attack generator (scratch only). Builds PATH shims named androguard and apktool
that decode nothing: each maps the INPUT FILE'S SHA-256 to a precomputed manifest. The two keys are
the authored fixture and the tampered copy the frozen probe writes (tamper is deterministic: the same
bump_last value and the same in-place ZIP patch on every run), so the lookup covers both legs."""
import hashlib, importlib.util, os, stat, sys
from pathlib import Path

FROZEN = Path(sys.argv[1]).resolve()          # frozen archive root
OUT = Path(sys.argv[2]).resolve()             # shim bin dir
spec = importlib.util.spec_from_file_location("probe", FROZEN / "reports/round-100/cap_apk_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

fixture = FROZEN / "corpus/fixtures/apk-r65"
apk_bytes = (fixture / "fixture.apk").read_bytes()
import json
truth = json.loads((fixture / "truth.json").read_text(encoding="utf-8"))
expected = probe.truth_values(truth)
fixture_sha = hashlib.sha256(apk_bytes).hexdigest()

import zipfile, io
with zipfile.ZipFile(io.BytesIO(apk_bytes)) as z:
    member = [n for n in z.namelist() if n.split("/")[-1] == "AndroidManifest.xml"][0]
    manifest = z.read(member)
tampered_value = probe.bump_last(expected["versionName"])
patched, why = probe.pool_patch(manifest, expected["versionName"], tampered_value)
assert patched is not None, why
new_apk, why = probe.patch_apk_member(apk_bytes, member, patched)
assert new_apk is not None, why
tamper_sha = hashlib.sha256(new_apk).hexdigest()


def xml(vn):
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
            '<manifest xmlns:android="http://schemas.android.com/apk/res/android" '
            f'package="{expected["package"]}" android:versionCode="{expected["versionCode"]}" '
            f'android:versionName="{vn}" />\n')


TRUTH_XML = xml(expected["versionName"])
TAMPER_XML = xml(tampered_value)

SHIM_TMPL = '''#!/usr/bin/env python3
# CriticR100 attack shim: lookup table keyed on the input file's sha256. Decodes nothing.
import hashlib, os, sys
FIXTURE_SHA = %r
TAMPER_SHA = %r
TRUTH_XML = %r
TAMPER_XML = %r
def digest(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def xml_for(p):
    d = digest(p)
    if d == FIXTURE_SHA:
        return TRUTH_XML
    if d == TAMPER_SHA:
        return TAMPER_XML
    return None
args = sys.argv[1:]
if args == ["--version"]:
    print("androguard lookup-shim 0.0 (attack)" if "%(NAME)s" == "androguard" else "apktool lookup-shim 0.0 (attack)")
    sys.exit(0)
if "%(NAME)s" == "androguard":
    if len(args) == 2 and args[0] == "axml":
        x = xml_for(args[1])
        if x is None:
            sys.stderr.write("unknown input\\n"); sys.exit(1)
        sys.stdout.write(x); sys.exit(0)
    sys.exit(2)
# apktool d -f -s -o <outdir> <apk>
if len(args) >= 5 and args[0] == "d":
    outdir = args[args.index("-o") + 1]
    apk = args[-1]
    x = xml_for(apk)
    if x is None:
        sys.stderr.write("unknown input\\n"); sys.exit(1)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "AndroidManifest.xml"), "w", encoding="utf-8").write(x)
    sys.exit(0)
sys.exit(2)
'''

OUT.mkdir(parents=True, exist_ok=True)
for name in ("androguard", "apktool"):
    p = OUT / name
    p.write_text(SHIM_TMPL % (fixture_sha, tamper_sha, TRUTH_XML, TAMPER_XML) if False else
                 SHIM_TMPL.replace("%(NAME)s", name) % (fixture_sha, tamper_sha, TRUTH_XML, TAMPER_XML),
                 encoding="utf-8")
    p.chmod(p.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
print("FIXTURE_SHA", fixture_sha)
print("TAMPER_SHA", tamper_sha)
print("TAMPERED_VERSIONNAME", tampered_value, "TRUTH_VERSIONNAME", expected["versionName"])
print("SHIMS", OUT)
