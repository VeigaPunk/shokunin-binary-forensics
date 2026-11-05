#!/usr/bin/env python3
"""ExecReceipts (round-95 w1) independent field audit of S500/S501 quote receipts.

Read-only over the frozen receipt chain. Checks, per sid:
  fetched_at == 2026-11-05
  http_status == 200
  fetch_url host in {raw.githubusercontent.com, github.com}
  sha256(committed raw body) == fetch_sha256
  receipt length == len(raw body bytes)
  fetch-log.md carries a line naming the sid AND the fetch_sha256
Extra context rows (clearly marked): strict JSON (no duplicate keys), receipt
sid/schema sanity, cross-check against the shas/lengths pinned in the frozen
reports/round-95/claims.md, body utf-8 decodability.

Prints a per-field PASS/FAIL table and FIELD_AUDIT_VERDICT=pass|fail.
Exit 0 iff every named check passes.
"""
import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
RECEIPTS = LANE / "reports" / "round-95" / "quote-receipts"
LOG = RECEIPTS / "fetch-log.md"
ALLOWED_HOSTS = {"raw.githubusercontent.com", "github.com"}
REQUIRED_FETCHED_AT = "2026-11-05"
# Values pinned in the frozen claims.md (S500/S501 receipt paragraphs).
FROZEN = {
    "S500": {"sha256": "69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f", "length": 17010},
    "S501": {"sha256": "f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac", "length": 18784},
}


def load_strict(path: Path):
    """json.loads that rejects duplicate keys."""
    def hook(pairs):
        keys = [k for k, _ in pairs]
        if len(keys) != len(set(keys)):
            dupes = sorted({k for k in keys if keys.count(k) > 1})
            raise ValueError(f"duplicate JSON keys: {dupes}")
        return dict(pairs)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    log_text = LOG.read_text(encoding="utf-8")
    log_lines = log_text.splitlines()
    any_fail = False

    for sid, frozen in FROZEN.items():
        rows = []
        rp = RECEIPTS / f"{sid}.receipt.json"
        bp = RECEIPTS / "raw" / f"{sid}.body"

        try:
            r = load_strict(rp)
            strict_detail = "strict JSON ok (no duplicate keys)"
            strict_ok = True
        except Exception as exc:  # noqa: BLE001 - audit must not crash on bad bytes
            r, strict_ok, strict_detail = {}, False, f"strict JSON load failed: {exc}"

        if bp.exists():
            body = bp.read_bytes()
        else:
            body = b""
        body_sha = sha256_hex(body)
        fetch_url = r.get("fetch_url", "")
        host = urlsplit(fetch_url).netloc.lower() if isinstance(fetch_url, str) else ""
        fetch_sha = r.get("fetch_sha256", "")
        log_hit = [
            ln.strip() for ln in log_lines
            if sid in ln and isinstance(fetch_sha, str) and fetch_sha and fetch_sha in ln
        ]

        checks = [
            ("fetched_at == 2026-11-05", r.get("fetched_at") == REQUIRED_FETCHED_AT,
             f"receipt={r.get('fetched_at')!r}"),
            ("http_status == 200", r.get("http_status") == 200,
             f"receipt={r.get('http_status')!r}"),
            ("fetch_url host allowed", host in ALLOWED_HOSTS,
             f"host={host!r} url={fetch_url}"),
            ("sha256(body) == fetch_sha256", body_sha == fetch_sha,
             f"body={body_sha} receipt={fetch_sha}"),
            ("length == len(body)", r.get("length") == len(body),
             f"receipt={r.get('length')!r} actual={len(body)}"),
            ("fetch-log line names sid + sha", bool(log_hit),
             (log_hit[0][:160] if log_hit else "no line carries both")),
            ("[extra] strict JSON, no dup keys", strict_ok, strict_detail),
            ("[extra] receipt sid == requested sid", r.get("sid") == sid,
             f"receipt={r.get('sid')!r}"),
            ("[extra] schema == revenger-quote-audit-v1",
             r.get("schema") == "revenger-quote-audit-v1", f"receipt={r.get('schema')!r}"),
            ("[extra] verdict == verified", r.get("verdict") == "verified",
             f"receipt={r.get('verdict')!r}"),
            ("[extra] body sha == frozen claims sha", body_sha == frozen["sha256"],
             f"body={body_sha} claims={frozen['sha256']}"),
            ("[extra] body length == frozen claims length", len(body) == frozen["length"],
             f"actual={len(body)} claims={frozen['length']}"),
            ("[extra] body non-empty and utf-8 decodable",
             len(body) > 0 and (body.decode("utf-8") or True) if body else False,
             f"bytes={len(body)}"),
        ]

        print(f"== {sid} ==")
        for name, ok, detail in checks:
            if not name.startswith("[extra]") and not ok:
                any_fail = True
            print(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
        print()

    print("FIELD_AUDIT_VERDICT=" + ("fail" if any_fail else "pass"))
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
