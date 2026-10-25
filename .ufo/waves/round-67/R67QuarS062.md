ABSENT — all 3 quoted strings confirmed missing from https://arxiv.org/html/2412.11539v1 (fetched real bytes, HTTP 200); register row S062 (campaign `revenger`, round1, `payload-absent`) absence claim verified.

# Seat
R67QuarS062 — wave-4 quarantine hand-check, item 10. Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` line 152 (READ-ONLY; shokuknow untouched).

# Fetch
- Command: `curl -sL --max-redirs 15 https://arxiv.org/html/2412.11539v1` (single attempt, no retries needed)
- Result: `http_code=200 size=446522 url=https://arxiv.org/html/2412.11539v1`
- sha256: `c353587e00a6652d35a89ad1ec1f895cf6fa372661d53ff07da6153693a13189` (446,522 bytes <= 2MB → saved whole)
- Saved: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S062/source.bin`
- Rendered variant: `quarantine/S062/rendered.txt` = python `html.unescape` + regex tag-strip of the raw bytes.
- Document identity: `<title>Android App Feature Extraction: A review of approaches for malware and app similarity detection</title>` — a real arXiv HTML page, not an error stub.

# Per-string results (fixed-string, case-sensitive)

## 1. `cell):` — ABSENT
- `grep -Fbo 'cell):' source.bin` → no hits. `html.unescape` find → -1; tag-stripped find → -1.
- Stronger: case-insensitive `grep -Fio 'cell[^<]\{0,20\}'` → zero hits; the literal "cell" occurs nowhere in the document, and no `cell):` exists under any entity encoding.
- Only `):` occurrence is byte offset 3807, inside a CSS comment: `/* Wide (the theme's 1280px): the theme lays the body out as a grid...` — stylesheet, not content.

## 2. `On Impact of Semantically Similar Apps in Android` — ABSENT
- `grep -Fbo` → no hits; unescaped/stripped find → -1.
- Case-insensitive probes: `Impact` → 0 hits anywhere; `Semantically`/`semantically` → 0 hits; `Similar Apps` → 0 hits case-sensitive (all 4 `similar apps` occurrences are lowercase body text).
- Near-miss (probable distortion source): the paper's own prose at byte offsets 167238 and 170873 reads `identify functionally similar apps with a two-stage clustering` / `deliver functionally similar apps was proposed by` (Al-Subaihin et al., 2016). "functionally similar apps" — not "Semantically Similar Apps" — is this document's actual phrase; no heading or cited-work title resembles the quoted string.

## 3. `In our experiments` — ABSENT
- `grep -Fbo` → no hits; unescaped/stripped find → -1.
- Case-insensitive `our experiments` → 0 hits; `experiment*` (case-insensitive) → 0 hits in the entire document — the review paper never uses the word "experiment" at all. `in our <word>` → 0 hits.

# Verdict basis
Fetch succeeded with real document bytes; every quoted string is missing under raw, entity-unescaped, and tag-stripped renderings. Fabrication-class absence confirmed for all three strings. No near-miss contradicts the register: the true sentences are `functionally similar apps` (Al-Subaihin et al., 2016, offsets 167238/170873) and the doc title `Android App Feature Extraction: A review of approaches for malware and app similarity detection`.

# Artifacts
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S062/source.bin`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S062/rendered.txt`

# Tooling
No installs or upgrades performed; curl/grep/python3 already present.
