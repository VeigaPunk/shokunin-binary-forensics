# CoreS059Review — round-72 wave 1 (S059, iBotPeaches/Apktool)

Seat: CoreS059Review-2 · Role: reviewer · Axes: coverage, source accuracy · Scope: S059 and its linked entry text only.

## Judgment: SUPPORT

No falsifying defect found. The pinned source resolves, the quote is verbatim at the cited anchor, the ≤25-word lesson Gate holds, and the entry's scope stays inside the README's own documented purpose with the required disclaimers. One documentation-precision note below; it does not touch the frozen C1 predicate.

## Evidence — source accuracy

### 1. Pinned commit resolves
- Locator claimed: `README.md "Apktool", commit 0312d212c713c9ebc568b7d9295eec0f47858bfa, accessed 2026-10-27` (corpus/SOURCES.md line 73).
- `https://raw.githubusercontent.com/iBotPeaches/Apktool/0312d212c713c9ebc568b7d9295eec0f47858bfa/README.md` returned the README (HTTP 200, text/plain). Control: the same URL at SHA `0000…0000` returns HTTP 404, so resolution is commit-SHA-sensitive; the 200 is real resolution, not a default-branch fallback.
- GitHub commit page for `0312d21` confirms: "docs: mark v3 as real and fix sponsor images (#4095)", authored by iBotPeaches, 1 file changed, README.md only, +5−5. The diff touches only the branch description line ("In-development Apktool 3.x branch" → "Apktool 3.x branch") and sponsor image URLs (`master` → `main`); the quoted paragraph appears only as untouched diff context (`@@ -9,7 +9,7 @@ Apktool is a tool for reverse engineering third-party, closed, binary, Android a…`).

### 2. Quote and anchor are exact
Pinned README paragraph under the level-3 heading `### Apktool` (retrieved byte-for-byte from the pinned URL):

> "Apktool is a tool for reverse engineering third-party, closed, binary, Android apps. It can decode resources to nearly original form and rebuild them after making some modifications; it makes it possible to debug smali code step-by-step. It also makes working with apps easier thanks to project-like file structure and automation of some repetitive tasks such as building apk, etc."

- SOURCES.md S059 quote: `It can decode resources to nearly original form and rebuild them after making some modifications` — verbatim 16-word substring ending exactly before the semicolon. 16 ≤ 25 words, satisfying the claim's "located quote ≤25 words in the lesson Gate".
- Anchor check: the quote lives in the first paragraph directly beneath the heading `### Apktool`; locator "README.md 'Apktool'" is accurate. (Heading is level-3 and is preceded by an italic website note; the locator does not claim a heading level, so no mismatch.)
- Lesson Gate row (knowledge/lessons/round-72.md line 18) repeats the same quote and the same "README 'Apktool'" anchor, ADMIT tier A "for the README's stated decode/rebuild role, not install validity or permission to modify third-party apps" — consistent with SOURCES.md.

### 3. Scope distinction — documented purpose vs reverse-engineering claims
The seat question: does the entry's scope distinguish the documented purpose from RE claims not made there?

- The README itself DOES state a reverse-engineering purpose in its first sentence: "Apktool is a tool for reverse engineering third-party, closed, binary, Android apps." So an RE-purpose claim IS made in the pinned source; it is not absent.
- The S059 row deliberately cites only the decode/rebuild clause and disclaims the rest: role reads "The repository's own stated Android resource/Smali decode and rebuild purpose; no APK correctness or permission claim", and the note adds "this entry does not claim the output is source-identical, install-valid, or appropriate for unlicensed modification." That is under-claiming relative to what the source permits — the safe direction.
- RE claims correctly NOT made by the entry: no execution, no installation, no output-correctness, no permission. The README's own permission sentence corroborates the boundary: "Apktool is **NOT** intended for piracy and other non-legal uses." The linked knowledge entry (corpus/knowledge/round-72-tool-landscape.md, row "Need Android/APK output views … Apktool S059") says "Apktool describes resource and Smali decoding and a rebuild path" with boundary "Decompiled or rebuilt files are not the original source or proof of install validity. The lane must remain static/artifact-first; no package is installed here." The entry's `verified-at` line states "No tool was installed or executed." No execution or installation is inferred from the README anywhere in the linked text.
- The README's "nearly original form" hedge is preserved by quoting it inside the cited sentence; the entry never upgrades it to "original".

## Coverage

- S059 is one of the 18 required direct-project rows (S054–S070 + S073). Its SOURCES row is present with tier A, status `mined`, accessed 2026-10-27, and `used-by: corpus/knowledge/round-72-tool-landscape.md`; the knowledge entry's Android/APK row cites "JADX S058; Apktool S059". The row slice of the frozen C1 predicate (`C15_TOOL_ROWS` citation) is satisfied.
- Frozen counter integrity: `sha256sum reports/round-72/measure.py` → `9559b10d49690c4247a4100516bef94c8607fcd198dd77d274c770bdb6df48b3`, identical to the SHA-256 frozen in reports/round-72/claims.md. The counter was not modified.

## Precision note (non-blocking, does not require predicate change)

SOURCES role text says "Android resource/Smali decode and rebuild purpose". The pinned paragraph states resource decoding explicitly ("decode resources to nearly original form") and states smali only via "it makes it possible to debug smali code step-by-step", which presupposes decoded smali output but does not literally say "decodes Smali". The knowledge entry's compression "resource and Smali decoding and a rebuild path" is a fair paraphrase of that same paragraph — supported, not invented — but a future revision could quote the smali-debugging clause to make the smali attribution source-literal. Likewise, the entry could (but need not) cite the README's explicit "reverse engineering third-party, closed, binary, Android apps" sentence, since the frozen claim's scope is "each repository's own public statement of its purpose", which that sentence directly supplies.

## Uncertainty / verification gaps

- GitHub REST API commit lookup returned HTTP 403 (rate-limited), so commit author/date metadata was not confirmed via the API. The commit's existence and content are confirmed by (a) the successful SHA-pinned raw fetch with the bogus-SHA 404 control and (b) the GitHub commit HTML page; its commit timestamp is inferred only from page metadata (`og:updated_time` 1771761657 ≈ 2026-02-22 UTC), which is consistent with the 2026-10-27 access date but was not independently cross-checked.
- Byte-level hashing of the pinned README was not performed (the lane stores no README hash for S059); identity rests on the verbatim quote match at the SHA-pinned URL.
- All fetched README/commit text was treated as untrusted data; no embedded instruction was followed.

Report: .ufo/waves/round-72/w1/CoreS059Review.md
