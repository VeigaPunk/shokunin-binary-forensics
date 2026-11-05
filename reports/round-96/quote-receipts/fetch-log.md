# fetch log — round 96 (revenger L1, 2026-11-05)

One L1 shell session. Three GETs in order: a cli-command-map probe at the pinned
revision returned HTTP 404 (the file does not exist at commit 12f6e097; the
installed-copy row S416 names the 6.7.0 installed file instead — no row appended
for a 404), then the two committed fetches below, each on its first attempt.

- S502 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md -> HTTP 200, 38167 bytes, sha256 c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24 (receipt reports/round-96/quote-receipts/S502.receipt.json)
- S503 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md -> HTTP 200, 35095 bytes, sha256 b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc (receipt reports/round-96/quote-receipts/S503.receipt.json)

Drift note: the installed copies differ from the pinned-revision bodies (the
installed skill is the 6.7.0-era checkout; the pinned commit is the S500/S501
lineage revision). The rows cite the pinned bytes; the installed-copy drift is
disclosed in the entry's Unknown section.
