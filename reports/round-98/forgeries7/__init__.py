#!/usr/bin/env python3
"""r97 mutator functions vendored verbatim from .ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py (sha256 56762e34f52b38b61ac53ededacda7cf6b6e4569f08ec61a4ed6a1f4ccb9cd80, see MANIFEST.sha256).

Provides: MUTATORS dict mapping short vector name (FR00, FR02, ...) to the r97 mutator callable.
Each callable signature: fn(root, mod) where mod is the counter-under-test module (or frozen v5 fallback) exposing ENTRY, VOTES_DIR, WAVE_DIR, RECEIPTS_DIR, digest, strict_json, cells, STATUS_ANY, ENTRY_REL, NA_NOTE, etc.
The original build_fresh.py binds `mod` as a global via its own frozen v5 import; here callers pass it explicitly.
`WAVE_DIR` in the original for FR05 references `mod.WAVE_DIR` ("web root" .ufo/waves/round-96) — preserved verbatim.
"""
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

_MOD = None
def set_mod(m):
    global mod
    mod = m

mod = None

def rd(p):
    return p.read_text(encoding="utf-8")


def wr(p, s):
    p.write_text(s, encoding="utf-8")


def jrd(p):
    return mod.strict_json(rd(p))


def jwr(p, obj):
    wr(p, json.dumps(obj, indent=1))


def rebind(root):
    """Re-sign the vote binding for an edited entry: new digest into every vote and artifact."""
    votes = sorted((root / mod.VOTES_DIR).glob("*.json"))
    old = jrd(votes[0])["candidate_sha256"]
    new = mod.digest(rd(root / mod.ENTRY))
    for vf in votes:
        v = jrd(vf)
        art = root / v["artifact_path"]
        b = rd(art).replace(old, new).encode("utf-8")
        art.write_bytes(b)
        v["candidate_sha256"] = new
        v["artifact_sha256"] = hashlib.sha256(b).hexdigest()
        jwr(vf, v)


def edit_row(root, rel, rowid, ncells, fn):
    p = root / rel
    lines = rd(p).split("\n")
    hits = [i for i, ln in enumerate(lines)
            if re.match(r"^ {0,3}\|", ln) and len(mod.cells(ln)) == ncells
            and mod.cells(ln)[0] == rowid]
    assert len(hits) == 1, (rel, rowid, len(hits))
    i = hits[0]
    lines[i] = "| " + " | ".join(fn(mod.cells(lines[i]))) + " |"
    wr(p, "\n".join(lines))


def swap_coverage_row(root, target, donor_line):
    p = root / "corpus/README.md"
    lines = rd(p).split("\n")
    hits = [i for i, ln in enumerate(lines)
            if re.match(r"^\|", ln) and len(mod.cells(ln)) == 5 and mod.cells(ln)[0] == target]
    assert len(hits) == 1, (target, len(hits))
    lines[hits[0]] = donor_line
    wr(p, "\n".join(lines))


def coverage_line(root, rowid):
    hits = [ln for ln in rd(root / "corpus/README.md").split("\n")
            if re.match(r"^\|", ln) and len(mod.cells(ln)) == 5 and mod.cells(ln)[0] == rowid]
    assert len(hits) == 1, (rowid, len(hits))
    return hits[0]


# ---- deltas (each: one class, one mutation or one named combination) ----

def m_none(root):
    return None


def m_usedby_case(root):
    # FR01: S502 used-by cell differs from the entry path in one letter's case
    def f(c):
        assert c[10] == mod.ENTRY_REL, c[10]
        return c[:10] + ["knowledge/Round-96-native-analysis-sessions.md"]
    edit_row(root, "corpus/SOURCES.md", "S502", 11, f)


def m_entry_bom(root):
    # FR02: UTF-8 BOM prepended to the admitted entry; votes re-signed to the new bytes
    p = root / mod.ENTRY
    wr(p, "\ufeff" + rd(p))
    rebind(root)


def m_c02_held_no_entry(root):
    # FR03: C02 held in the README, candidate entry file removed from the tree
    (root / mod.ENTRY).unlink()


def m_c02_plus_other_row(root):
    # FR04: C02 flipped to held AND an unrelated row (C14) re-worded in the same change
    edit_row(root, "corpus/README.md", "C14", 5,
             lambda c: c[:3] + [c[3] + " (re-verified 2026-11-05)"] + c[4:])


def m_vote_foreign_sha(root):
    # FR05: CriticR96 candidate digest correct; artifact_sha256 is the sha of ReviewerGate's file
    vf = root / mod.VOTES_DIR / "CriticR96.json"
    v = jrd(vf)
    other = (root / mod.WAVE_DIR / "w1/ReviewerGate/gate-evidence.md").read_bytes()
    v["artifact_sha256"] = hashlib.sha256(other).hexdigest()
    jwr(vf, v)


def m_row_dup_held_over_held(root):
    # FR06: held C06 coverage row replaced by a copy of held C01 (C02 held) -> K 13/15, C06 gone
    swap_coverage_row(root, "C06", coverage_line(root, "C01"))


def m_row_dup_target_over_held(root):
    # FR07: held C06 coverage row replaced by a copy of the flipped C02 row -> K 13/15, C06 gone
    swap_coverage_row(root, "C06", coverage_line(root, "C02"))


def m_headers_in_fence(root):
    # FR08: the three provenance headers wrapped in a text fence (shown as example, not header)
    p = root / mod.ENTRY
    t = rd(p).split("\n")
    si = next(i for i, l in enumerate(t) if mod.STATUS_ANY.search(l))
    t = ["```text"] + t[:si] + ["```"] + t[si:]
    wr(p, "\n".join(t))
    rebind(root)


def m_verified_at_stale(root):
    # FR09: verified-at header moved to 2026-10-01; receipts still fetched 2026-11-05; votes re-signed
    p = root / mod.ENTRY
    t = rd(p)
    assert "verified-at: 2026-11-05" in t
    wr(p, t.replace("verified-at: 2026-11-05", "verified-at: 2026-10-01", 1))
    rebind(root)


def m_na_boilerplate_on_pass(root):
    # FR10: ReviewerGate flips a PASS (Q09) to n/a with the shared boilerplate reason
    vf = root / mod.VOTES_DIR / "ReviewerGate.json"
    v = jrd(vf)
    assert v["decisions"]["Q09"] == "PASS"
    v["decisions"]["Q09"] = "n/a"
    v["notes"]["Q09"] = mod.NA_NOTE
    jwr(vf, v)


def m_receipt_owner_swap(root):
    # FR11: S502 receipt fetch_url owner swapped (allowlisted host kept); body and hash untouched
    rp = root / mod.RECEIPTS_DIR / "S502.receipt.json"
    r = jrd(rp)
    assert "/morluto/rea/" in r["fetch_url"], r["fetch_url"]
    r["fetch_url"] = r["fetch_url"].replace("/morluto/rea/", "/attacker-fork/rea/", 1)
    jwr(rp, r)


def m_own_work_dangling(root):
    # FR12: S504 own-work record pointer names a saved-session path that does not exist
    def f(c):
        assert "corpus/live/runs/round-96/" in c[1], c[1]
        return [c[0], c[1].replace("corpus/live/runs/round-96/",
                                   "corpus/live/runs/round-96-r97-missing/")] + c[2:]
    edit_row(root, "corpus/SOURCES.md", "S504", 11, f)



def m_entry_bom_unsigned(root):
    # FR02b: as FR02 but votes NOT re-signed (post-vote edit with stale vote binding)
    p = root / mod.ENTRY
    wr(p, "\ufeff" + rd(p))


def m_headers_in_fence_unsigned(root):
    # FR08b: as FR08 but votes NOT re-signed
    p = root / mod.ENTRY
    t = rd(p).split("\n")
    si = next(i for i, l in enumerate(t) if mod.STATUS_ANY.search(l))
    wr(p, "\n".join(["```text"] + t[:si] + ["```"] + t[si:]))


def m_verified_at_stale_unsigned(root):
    # FR09b: as FR09 but votes NOT re-signed
    p = root / mod.ENTRY
    t = rd(p)
    assert "verified-at: 2026-11-05" in t
    wr(p, t.replace("verified-at: 2026-11-05", "verified-at: 2026-10-01", 1))


VECTORS = [
    ("FR00-honest-control", "control", "none: honest v5 _fixture() tree", m_none, "pass"),
    ("FR01-usedby-case-path", "used-by path-form (case-only)",
     "S502 used-by cell knowledge/round-96-... -> knowledge/Round-96-... (one letter case)",
     m_usedby_case, "FAIL"),
    ("FR02-entry-leading-bom", "entry bytes (BOM)",
     "UTF-8 BOM prepended to the admitted entry; votes re-signed to the new digest",
     m_entry_bom, "FAIL"),
    ("FR03-c02-held-entry-absent", "README vs tree",
     "C02 flipped held (fixture), candidate entry file deleted from the tree",
     m_c02_held_no_entry, "FAIL"),
    ("FR04-c02-held-plus-other-row", "README one-row-only",
     "C02 flipped held AND C14 evidence cell re-worded in the same change",
     m_c02_plus_other_row, "FAIL"),
    ("FR05-vote-foreign-artifact-sha", "vote artifact binding",
     "CriticR96 candidate digest correct; artifact_sha256 = sha of ReviewerGate's artifact",
     m_vote_foreign_sha, "FAIL"),
    ("FR06-row-dup-held-over-held", "coverage row set",
     "held C06 row replaced by a copy of held C01 row (C02 held; K computed 13/15)",
     m_row_dup_held_over_held, "FAIL"),
    ("FR07-row-dup-target-over-held", "coverage row set",
     "held C06 row replaced by a copy of the flipped C02 row (K computed 13/15)",
     m_row_dup_target_over_held, "FAIL"),
    ("FR08-headers-in-fence", "provenance header",
     "source/verified-at/recheck/coverage-map headers wrapped in a ```text fence; votes re-signed",
     m_headers_in_fence, "FAIL"),
    ("FR09-verified-at-stale", "provenance date",
     "verified-at 2026-11-05 -> 2026-10-01 while receipts say fetched 2026-11-05; votes re-signed",
     m_verified_at_stale, "FAIL"),
    ("FR10-na-boilerplate-on-pass", "vote decision",
     "ReviewerGate Q09 PASS -> n/a with the shared NA_NOTE boilerplate reason",
     m_na_boilerplate_on_pass, "FAIL"),
    ("FR11-receipt-owner-swap", "receipt fetch identity",
     "S502 receipt fetch_url owner morluto -> attacker-fork (allowlisted host), body and hash intact",
     m_receipt_owner_swap, "FAIL"),
    ("FR12-own-work-dangling", "own-work record pointer",
     "S504 SOURCES pointer corpus/live/runs/round-96/ -> corpus/live/runs/round-96-r97-missing/",
     m_own_work_dangling, "FAIL"),
    ("FR02b-entry-bom-unsigned", "entry bytes (BOM), stale vote binding",
     "as FR02 but the entry changed after the votes and votes not re-signed",
     m_entry_bom_unsigned, "FAIL"),
    ("FR08b-headers-in-fence-unsigned", "provenance header, stale vote binding",
     "as FR08 but the entry changed after the votes and votes not re-signed",
     m_headers_in_fence_unsigned, "FAIL"),
    ("FR09b-verified-at-stale-unsigned", "provenance date, stale vote binding",
     "as FR09 but the entry changed after the votes and votes not re-signed",
     m_verified_at_stale_unsigned, "FAIL"),
]



MUTATORS = {
    "FR00": m_none,
    "FR02": m_entry_bom,
    "FR06": m_row_dup_held_over_held,
    "FR07": m_row_dup_target_over_held,
    "FR08": m_headers_in_fence,
    "FR09": m_verified_at_stale,
    "FR10": m_na_boilerplate_on_pass,
    "FR12": m_own_work_dangling,
}
