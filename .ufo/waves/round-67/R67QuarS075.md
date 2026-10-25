ABSENT — all three quoted strings are missing from the fetched source (HTTP 200, real mjs bytes); register row S075 (round2, `payload-absent`) re-derives as confirmed.

# Scope
- Register row: /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:155 — `revenger | round2 | S075 | payload-absent`
- Cited source: https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/verify/android/analysis.mjs
- Register note: "cited source, companion URLs and local artifacts were all checked; the quote is in none of them"

# Fetch receipt
- Command: `curl -sL --max-redirs 15 -o source.bin <URL>` (1 attempt, no retries needed)
- HTTP_CODE=200, SIZE=10289, effective URL unchanged (no redirect chase)
- Saved bytes: /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S075/source.bin (10289 bytes ≤ 2MB)
- sha256: `a3b6f712151121242f14535b40dbe5745c065c2189a09adfd2f2a41eccd40e8f`
- Document is a real Node.js verifier script (317 lines, `import { verifyAndroidCliCancellation } ...`, MCP client `rea-real-android-verifier`), not a 404/error page.

# Per-string results (grep -F, case-sensitive; also tested on html.unescape + tag-stripped rendering — file is plain JS, no HTML entities/tags present)

1. `Caller-supplied engine` — ABSENT
   - raw: `grep -F -c` → 0; unescaped rendering: not found; tag-stripped: not found.
   - Component fragments: `Caller` 0 hits, `Caller-supplied` 0 hits, `supplied` 0 hits. `engine` 1 hit only at line 295: `engine: packageResult.engine,` — a report-object field echoing the analyzer's self-reported engine, not caller-supplied anything. Case-insensitive scan for `caller|engine|resource` matched only line 295.
   - Near-miss named: `engine: packageResult.engine,` (source.bin:295) is the probable sentence the quote distorted.
   - Escaped variants `Caller&#x27;s`, `Caller-supplied&#x2D;engine`: 0 hits.

2. `Resource policy and verification` — ABSENT
   - raw: `grep -F -c` → 0; unescaped/tag-stripped: not found.
   - Component fragments: `Resource` 0 hits, `Resource policy` 0 hits, `policy` 0 hits. `verification` 1 hit only at line 238: `assert.equal(packageResult.signature_verification, "not_performed");` — a package-signature field name, unrelated to resource policy.
   - Near-miss named: `signature_verification` (source.bin:238); the file's only "policy"-adjacent vocabulary is the verify* function family (`verifyAndroidMetadata`, `verifyAndroidClassSearch`, etc.), none containing `policy` or `resource`.

3. `Caller-supplied engine` (second occurrence listed in register) — ABSENT, identical finding to string 1 (register lists the same literal twice).

# Verdict
- Row S075 verdict: **ABSENT** — fabrication-class confirmation. The strings are not in the cited source; closest real content is `engine: packageResult.engine` (line 295) and `packageResult.signature_verification` (line 238), which the fabricated phrases appear to have embellished into policy/engine claims.

# Bounds / tooling
- No tool installs performed or needed (curl, grep, python3 stdlib already present).
- Reads: register row (read-only), cited URL. Writes: only under .ufo/waves/round-67/quarantine/S075/ and this report. No corpus/git mutations.
