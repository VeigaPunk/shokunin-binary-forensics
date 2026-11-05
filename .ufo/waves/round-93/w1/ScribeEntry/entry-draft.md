source: S495 — Saved r77 CDP browser-runtime record and its authored fixture — `corpus/live/runs/round-77/` and `corpus/fixtures/browser-r77/` (own-work, tier A, opened 2026-11-05) — anchors: `corpus/live/runs/round-77/inspection.json` stdout sha256 `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`; `corpus/live/runs/round-77/receipt.json` exit_code 0; `corpus/live/runs/round-77/LEDGER.md` record entry; fixture `corpus/fixtures/browser-r77/index.html` sha256 `46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45` and `corpus/fixtures/browser-r77/app.js` sha256 `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593` — grounds every identity fact this entry states about the saved round-77 CDP record and its authored fixture, and no claim about any other browser, Chrome, CDP or Electron
source: S496 — Chrome DevTools Protocol — https://chromedevtools.github.io/devtools-protocol/ (docs, tier A, opened 2026-11-05) — anchor: landing-hero intro paragraph, second sentence (CDP self-description); HTTP Last-Modified 2026-11-04, ETag `6aeab6b6-8a86` — "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers." — grounds the one external sentence this entry states, that CDP is the protocol Chrome exposes for inspecting and debugging pages; cited for that self-description only, not for any compatibility or stability guarantee
verified-at: 2026-11-05 at lane commit `02050cb2a6758e3bd9cec696ff0e42df6f23511a` (`git rev-parse 02050cb2a6758e3bd9cec696ff0e42df6f23511a^{commit}` prints `02050cb2a6758e3bd9cec696ff0e42df6f23511a`; `git diff --quiet 02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus` is silent, so the corpus tree read here is byte-identical at that commit)
recheck: `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json` from the lane root — exit 0 with `ORACLE OK (17/17 checks)` as its last stdout line; the same command and its full stdout are in the `## Reproduce` section below, and the sibling one-liners that re-derive this entry's other record fields are quoted verbatim in the Observation section below
coverage-map: C08 (`corpus/README.md`, browser/Electron runtime evidence) — the ground this entry covers is the two authored inert files `corpus/fixtures/browser-r77/index.html` and `corpus/fixtures/browser-r77/app.js` and the one saved round-77 CDP record `corpus/live/runs/round-77/`; no other browser, Chrome, CDP or Electron surface is claimed
admission-status: candidate

# Browser/CDP runtime evidence in one authored inert fixture, checked against the lane's saved round-77 record — C08

Scope. One provider operation, one authored inert fixture of two static files, and one saved producer record of that
fixture. The analysis is **manual**: the lane's own committed oracle script re-derives the fixture's authored anchors
from the committed bytes and compares what it derived against what the saved record says. Nothing was loaded,
executed, served, fetched or decompiled; no producer was invoked for this entry; no network call was made; no
credential material appears in this entry or in the records it reads.

The fixture is `corpus/fixtures/browser-r77/` (`index.html`, `app.js`, `truth.json`, `oracle_check.py`). The record is
`corpus/live/runs/round-77/inspection.json` — the producer's exact stdout bytes for one `inspect_web_page` call over
that fixture — with `corpus/live/runs/round-77/receipt.json` and `corpus/live/runs/round-77/LEDGER.md` beside it.

## 1. Observation

**Reading rule for the blocks below.** Each `$ ` block is one command's verbatim stdout, run from the lane root; the
command line above it is the exact argv that produced the lines below it. Each `transcript` block is likewise one
command's verbatim stdout for a one-liner that reads the committed record or the committed fixture bytes; a one-liner
is written as a `python3 -c` program, which the lane's frozen embedded-output gate
(`corpus/check_embedded_outputs.py`) deliberately refuses to replay, so those blocks are quoted as transcripts and are
not re-executed by that gate. The gate re-derives the entry's identity facts through the `$ ` oracle block instead,
whose stdout is reproduced in full in `## Reproduce`. The item numbers below are this entry's own and are not
identifiers in any file.

**1. The producer's identity fields and the record's own target facts.** The oracle's `operation == inspect_web_page`
and `provider.id == rea-cdp-browser` checks read the record's own fields; the target lines read the record's
`normalized_result.target` and `normalized_result.frames[0]`; the `evidence_id shape ev_<64hex>` check reads only the
*shape* of the record's `evidence_id`, never its value.


```
$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json
check ok: fixture index.html sha256+len match truth.json
check ok: fixture app.js sha256+len match truth.json
check ok: authored anchors derived from index.html bytes
check ok: operation == inspect_web_page
check ok: provider.id == rea-cdp-browser
check ok: evidence_id shape ev_<64hex>
check ok: target.url == http://127.0.0.1:8477/index.html
check ok: target.origin == http://127.0.0.1:8477
check ok: target.title == derived 'r77 probe page [loaded]'
check ok: target.type page and frames[0].url == page_url
check ok: metadata.dom_urls == exactly the app.js src
check ok: scripts.items count == 2 with page + app.js urls
check ok: app.js script length == 101 and reconciliation exact
check ok: inline script length == 46 (from index.html bytes)
check ok: app.js cdp_hash == sha256(committed app.js bytes)
check ok: inline script cdp_hash == sha256(inline text from index.html bytes)
check ok: resources == 1 app.js entry, content_size 101, text/javascript
ORACLE OK (17/17 checks)
```

The record's literal values for those fields, read back from the committed record bytes, are the transcript below
(`operation`, `predicate_type`, `provider.id`, `provider.version` are record fields; `evidence_id.shape` is the
shape test the oracle also runs):


```
transcript — python3 -B -c 'import json,re;d=json.load(open("corpus/live/runs/round-77/inspection.json"));print("operation",d["operation"]);print("predicate_type",d["predicate_type"]);print("provider.id",d["provider"]["id"]);print("provider.version",d["provider"]["version"]);print("evidence_id",d["evidence_id"]);print("evidence_id.shape",bool(re.fullmatch(r"ev_[0-9a-f]{64}",d["evidence_id"])))'
operation inspect_web_page
predicate_type rea.web-page-inspection
provider.id rea-cdp-browser
provider.version 2
evidence_id ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd
evidence_id.shape True
```

**2. The target, the DOM script url, the script inventory and the single resource.** The oracle's
`target.type page and frames[0].url == page_url`, `metadata.dom_urls == exactly the app.js src`,
`scripts.items count == 2 with page + app.js urls` and `resources == 1 app.js entry, content_size 101, text/javascript`
checks read those fields of the same record; the transcript re-reads them and prints the resource's `type`,
`mime_type` and `content_size` and each script item's `resource_reconciliation` status, which the oracle compares
but does not print.


```
transcript — python3 -B -c 'import json;d=json.load(open("corpus/live/runs/round-77/inspection.json"));n=d["normalized_result"];t=n["target"];print("target.type",t["type"]);print("target.url",t["url"]);print("target.origin",t["origin"]);print("target.title",t["title"]);print("frames[0].url",n["frames"][0]["url"]);print("metadata.dom_urls",json.dumps(n["metadata"]["dom_urls"]));print("scripts.total",n["scripts"]["total"]);print("resources count",len(n["resources"]));print("resource",n["resources"][0]["type"],n["resources"][0]["mime_type"],n["resources"][0]["content_size"],n["resources"][0]["url"]);print("app.js script reconciliation",[i["resource_reconciliation"]["status"] for i in n["scripts"]["items"] if i["url"].endswith("/app.js")][0]);print("inline script reconciliation",[i["resource_reconciliation"]["status"] for i in n["scripts"]["items"] if i["url"].endswith("/index.html")][0])'
target.type page
target.url http://127.0.0.1:8477/index.html
target.origin http://127.0.0.1:8477
target.title r77 probe page [loaded]
frames[0].url http://127.0.0.1:8477/index.html
metadata.dom_urls [{"node_index": 10, "attribute": "src", "url": "http://127.0.0.1:8477/app.js", "destination_scope": "approved"}]
scripts.total 2
resources count 1
resource Script text/javascript 101 http://127.0.0.1:8477/app.js
app.js script reconciliation exact
inline script reconciliation unmatched
```

**3. The two script lengths, derived from the committed fixture bytes.** The oracle derives the inline script's
length from the `<script>` body it reads out of the committed `index.html` bytes and compares it with the record's
`scripts.items[].length`; the transcript measures the same two committed files and prints the record's two script
lengths beside them.


```
transcript — python3 -B -c 'import json,pathlib;idx=pathlib.Path("corpus/fixtures/browser-r77/index.html").read_bytes();app=pathlib.Path("corpus/fixtures/browser-r77/app.js").read_bytes();d=json.load(open("corpus/live/runs/round-77/inspection.json"));items=d["normalized_result"]["scripts"]["items"];print("index.html byte length",len(idx));print("app.js byte length",len(app));print("record scripts.total",d["normalized_result"]["scripts"]["total"]);print("record script lengths",sorted(i["length"] for i in items));print("record script urls",sorted(i["url"] for i in items))'
index.html byte length 316
app.js byte length 101
record scripts.total 2
record script lengths [46, 101]
record script urls ['http://127.0.0.1:8477/app.js', 'http://127.0.0.1:8477/index.html']
```

**4. Both `cdp_hash` values equal the sha256 of the authored script texts.** The oracle's
`app.js cdp_hash == sha256(committed app.js bytes)` and
`inline script cdp_hash == sha256(inline text from index.html bytes)` checks compare the record's two `cdp_hash`
fields with digests the script computes over the committed bytes; the transcript prints both digests and both
record values so the two sides are visible side by side.


```
transcript — python3 -B -c 'import hashlib,json,pathlib,re;idx=pathlib.Path("corpus/fixtures/browser-r77/index.html").read_text();app=pathlib.Path("corpus/fixtures/browser-r77/app.js").read_bytes();body=[b for a,b in re.findall(r"<script([^>]*)>(.*?)</script>",idx,re.S) if "src=" not in a][0];d=json.load(open("corpus/live/runs/round-77/inspection.json"));items={i["url"].rsplit("/",1)[-1]:i for i in d["normalized_result"]["scripts"]["items"]};a=hashlib.sha256(app).hexdigest();s=hashlib.sha256(body.encode("utf-8")).hexdigest();print("app.js byte length",len(app),"sha256",a);print("record app.js cdp_hash",items["app.js"]["cdp_hash"]);print("app.js cdp_hash equals sha256(committed bytes)",a==items["app.js"]["cdp_hash"]);print("inline script text length",len(body),"sha256",s);print("record inline cdp_hash",items["index.html"]["cdp_hash"]);print("inline cdp_hash equals sha256(inline text from index.html bytes)",s==items["index.html"]["cdp_hash"])'
app.js byte length 101 sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593
record app.js cdp_hash fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593
app.js cdp_hash equals sha256(committed bytes) True
inline script text length 46 sha256 ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783
record inline cdp_hash ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783
inline cdp_hash equals sha256(inline text from index.html bytes) True
```

**5. The record's own bytes, the receipt's pin and the two fixture digests.** The transcript re-hashes the committed
record file, the committed `index.html` and the committed `app.js`, and compares the record's digest with the
`stdout_sha256` the saved receipt records; the oracle separately re-hashes both fixture files against the authored
premise file `corpus/fixtures/browser-r77/truth.json` on every run (its first two check lines).


```
transcript — python3 -B -c 'import hashlib,json,pathlib;rec=pathlib.Path("corpus/live/runs/round-77/inspection.json");b=rec.read_bytes();rcpt=json.load(open("corpus/live/runs/round-77/receipt.json"));print("inspection.json byte length",len(b));print("inspection.json sha256",hashlib.sha256(b).hexdigest());print("receipt.stdout_sha256",rcpt["stdout_sha256"]);print("record sha256 equals receipt stdout_sha256",hashlib.sha256(b).hexdigest()==rcpt["stdout_sha256"]);print("receipt.exit_code",rcpt["exit_code"]);print("receipt.duration_seconds",rcpt["duration_seconds"]);print("receipt.producer",rcpt["producer"]);print("index.html sha256",hashlib.sha256(pathlib.Path("corpus/fixtures/browser-r77/index.html").read_bytes()).hexdigest());print("app.js sha256",hashlib.sha256(pathlib.Path("corpus/fixtures/browser-r77/app.js").read_bytes()).hexdigest())'
inspection.json byte length 10816
inspection.json sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868
receipt.stdout_sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868
record sha256 equals receipt stdout_sha256 True
receipt.exit_code 0
receipt.duration_seconds 3.498
receipt.producer rea 6.8.0 (installed CLI; provider rea-cdp-browser, built-in; browser surface is the host's own Chrome/156.0.8078.74 headless on loopback CDP — no engine installed or updated)
index.html sha256 46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45
app.js sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593
```

**6. The fields that change from run to run.** The volatile list is the authored premise file's own
`volatile_not_compared` array, quoted verbatim from the committed `truth.json`; the transcript prints that array and
nothing else.


```
transcript — python3 -B -c 'import json;print(json.dumps(json.load(open("corpus/fixtures/browser-r77/truth.json"))["volatile_not_compared"],indent=1))'
[
 "evidence_id (fresh per run; only its shape is checked)",
 "target.target_id and frame_id (per browser launch)",
 "scripts.items[].script_key and .cdp_hash (per parse/session)",
 "capture_window timestamps (wall clock)",
 "completeness counters (attach- and policy-dependent)"
]
```

The capture window, the completeness status, the browser product string and the record's own `confidence` and
`authority` fields are **recorded** fields of the saved record — the transcript reads them back and prints them, and
no command in this entry compares them against anything outside the record:


```
transcript — python3 -B -c 'import json;d=json.load(open("corpus/live/runs/round-77/inspection.json"));n=d["normalized_result"];print("capture_window",json.dumps(n["capture_window"]));print("completeness.status",n["completeness"]["status"]);print("browser.product",n["browser"]["product"]);print("record confidence",d["confidence"],"authority",d["authority"])'
capture_window {"started_at": "2026-11-01T06:59:28.999Z", "ended_at": "2026-11-01T06:59:29.701Z", "observation_ms": 500}
completeness.status policy_filtered
browser.product Chrome/156.0.8078.74
record confidence observed authority external-service
```

**7. What the external row adds.** S496's located quote — the second sentence of the DevTools Protocol landing
page's intro paragraph — states that CDP is the protocol Chrome exposes so that clients can instrument, inspect,
debug and profile browsers. That is the only external sentence this entry states, and it is what makes the saved
record describable as a CDP inspection record rather than an unnamed page observation. It says nothing about this
lane's fixture, this lane's producer, or any other browser family.

## 2. Inference

8. [INFERENCE, scoped to this fixture and this record] The producer's two `cdp_hash` values are content digests of
the two authored script texts, not opaque identifiers: each equals the sha256 of the corresponding authored text
recomputed from the committed fixture bytes. Basis: item 4's two transcript lines and the oracle's two `cdp_hash`
check lines, item 1's oracle block.

9. [INFERENCE, scoped to this fixture and this record] The record's `target.title` is the authored page's static
title plus the string literal in the authored inline script, so the inline script ran in the observed page. Basis:
the oracle's `target.title == derived 'r77 probe page [loaded]'` line, whose expectation the script derives from the
committed `index.html` bytes, against item 2's `target.title` transcript line.

10. [INFERENCE, scoped to this fixture and this record] The record describes exactly one resource, the external
`app.js`, and the producer reconciled the `app.js` script item to that resource with status `exact` while the inline
script item is `unmatched`. Basis: item 2's transcript lines `resources count`, `resource`, `app.js script
reconciliation` and `inline script reconciliation`, and the oracle's `app.js script length == 101 and
reconciliation exact` line.

11. [INFERENCE] Each digest in this entry binds exactly the bytes it was computed over: the fixture digests bind the
two fixture files, the two `cdp_hash` values bind the two authored script texts, and the record's digest binds the
saved record file's bytes. A digest match is not evidence of origin, completeness, authenticity, or a valid
interpretation. Basis: items 4 and 5.

12. [INFERENCE] The saved record is a producer-derived observation of one authored page, made by one provider
operation against one local origin, and the lane's own oracle re-derives that the record's identity fields still bind
to the committed fixture bytes today. That the record was complete, or that a fresh run would produce the same bytes,
is not inferred. Basis: items 1, 2, 5 and 6.

## 3. Unknown

13. Whether the producer's CDP observation is correct or complete for any page, origin, browser or browser version
other than this authored fixture is **unknown**. This entry examines one inert fixture and one saved record.

14. Whether a fresh run of the producer would reproduce these bytes is **unknown**: the volatile list in item 6 names
the `evidence_id`, the `target_id` and `frame_id`, the `script_key` and `cdp_hash` fields, the capture-window
timestamps and the completeness counters as per-run values, and no producer was re-run for this entry.

15. Why the inline script item's `resource_reconciliation` status is `unmatched` while the `app.js` item's is
`exact` is **unknown**. The record's own reason string for the unmatched case is not printed by any command here, and
the entry reports the two statuses without explaining them.

16. Why the record's `completeness.status` is `policy_filtered` and which sections that filtered out is **unknown**
from the record's summary fields alone; the record's own `limitations` array is a **recorded** field of the saved
file and no command in this entry re-derives it.

17. Whether the recorded `capture_window` timestamps, the recorded browser product string and the recorded
`confidence` / `authority` values are accurate is **unknown**. They are read back from the saved record and compared
with nothing outside it.

18. Whether the saved record is authentic, complete or correctly attributed to the producer that wrote it is
**unknown**. The digest comparison in item 5 is a byte-identity check between two committed files, nothing more.

## 4. Limitations

19. **Fixture-scoped.** One authored inert fixture of two static files — `index.html`, whose only scripted behaviour
is an inline script that appends a string literal to the document title, and `app.js`, whose only scripted behaviour
is one assignment to a global probe object — and one saved round-77 CDP record. Nothing here is a claim about Chrome,
CDP, Electron, any other browser, or any page this lane did not author.

20. **One saved run.** One record, one capture window, one target. The recheck command re-derives this entry's
numbers against these committed bytes; it does not re-observe anything and it is not a probe of any live surface.

21. **No producer readiness claim.** No producer was invoked for this entry, on this host or at this time. The
`receipt.json` fields that record the earlier round-77 run — its `exit_code`, its `duration_seconds`, its
`stdout_sha256` and its `producer` string — are **recorded** fields of that saved file; this entry re-derives the
record's digest against the receipt's `stdout_sha256` and makes no claim that any producer is installed, available or
usable now.

22. **No authenticity claim.** Every digest here binds bytes only. No digest in this entry is offered as proof of
producer origin, acquisition completeness, or a valid interpretation of the record.

23. **No execution, no serving, no network.** The fixture bytes were parsed by the lane's own committed scripts; the
producer was not invoked, the fixture was not served, the browser was not launched, and no request left this host.

24. **Which side of each comparison is a byte reading.** Every check the entry leans on compares a record field (or
the committed fixture bytes) with an expectation, and each expectation has one of three sides. The table below names
the check names per side; a check name that appears in one column appears in no other column.

| expectation re-derived from the committed fixture bytes | expectation fixed in the authored premise file (`corpus/fixtures/browser-r77/truth.json`) | expectation a literal in the oracle script |
|---|---|---|
| `authored anchors derived from index.html bytes`, `target.title == derived 'r77 probe page [loaded]'`, `inline script length == 46 (from index.html bytes)`, `app.js cdp_hash == sha256(committed app.js bytes)`, `inline script cdp_hash == sha256(inline text from index.html bytes)` | `fixture index.html sha256+len match truth.json`, `fixture app.js sha256+len match truth.json`, `operation == inspect_web_page`, `provider.id == rea-cdp-browser`, `target.url == http://127.0.0.1:8477/index.html`, `target.origin == http://127.0.0.1:8477`, `target.type page and frames[0].url == page_url`, `scripts.items count == 2 with page + app.js urls` | `evidence_id shape ev_<64hex>` |

Three checks mix a byte-derived side with a fixed or literal side, so they are named in neither column.
`app.js script length == 101 and reconciliation exact` compares the record's script length with the byte length of
the committed `app.js` bytes, and compares the record's reconciliation status with the literal `exact` in the
script. `metadata.dom_urls == exactly the app.js src` compares the dom-url's `url` with the origin and script path
the premise file names, and the dom-url's `attribute` with the literal `src` in the script. `resources == 1 app.js entry, content_size 101, text/javascript` compares the resource count with the
premise file's `producer_expected.resource_count`, the resource's `content_size` with the byte length of the
committed `app.js` bytes, the resource's mime type with the premise file's `producer_expected.resource_mime`, and
the resource's url with the path the premise file's `authored.external_script_path` names.
An `OK` verdict on a pin or hypothesis line shows agreement with a value fixed in advance, not with an independent
parse.

25. **The record-file digests are recorded, not re-hashed by the oracle.** The `stdout_sha256` value in the saved
`receipt.json` is a **recorded** field of that file; the transcript in item 5 re-hashes the committed record file
and compares it with that recorded value, which is a byte-identity check between two committed files and not a
producer-origin claim.

26. **No guard credit beyond re-derivation.** The recheck command re-derives the numbers it prints and exits
non-zero when a comparison fails; it detects no deletion of a clause, a table row or a sentence of this entry, and
it does not re-observe any page. The one-liner transcripts in items 1, 2, 3, 4, 5 and 6 are not re-executed by
`corpus/check_embedded_outputs.py`, whose confinement admits only `python3 [-B] <script inside the tree> [args]`
commands; the `$ ` oracle block is the part of this entry that gate replays.

27. **The parser is the lane's own.** The byte-level readings come from the lane's own committed oracle script, which
is lane code and not an independent third-party reader, and which reads the same two fixture files the record was
made from.

## 5. Provenance (Q11)

Every count, identifier and digest printed above is carried by one of the commands below, and the line that carries
it is named here together with the side the script compared it against.

| # | what it states | command | the stdout line that carries it | the expectation side |
|---|---|---|---|---|
| 1 | the operation, the provider id, the `evidence_id` shape, the pinned url and origin, the derived title, the target type and frame url, the dom-url set, the script count and urls, both script lengths, both `cdp_hash` bindings, the single resource's size and mime type, and the fixture-byte re-hash of both fixture files | the r77 oracle (`$ ` block in item 1, reproduced in `## Reproduce`) | `check ok: operation == inspect_web_page`, `check ok: provider.id == rea-cdp-browser`, `check ok: evidence_id shape ev_<64hex>`, `check ok: target.url == http://127.0.0.1:8477/index.html`, `check ok: target.origin == http://127.0.0.1:8477`, `check ok: target.title == derived 'r77 probe page [loaded]'`, `check ok: target.type page and frames[0].url == page_url`, `check ok: metadata.dom_urls == exactly the app.js src`, `check ok: scripts.items count == 2 with page + app.js urls`, `check ok: app.js script length == 101 and reconciliation exact`, `check ok: inline script length == 46 (from index.html bytes)`, `check ok: app.js cdp_hash == sha256(committed app.js bytes)`, `check ok: inline script cdp_hash == sha256(inline text from index.html bytes)`, `check ok: resources == 1 app.js entry, content_size 101, text/javascript` | the sides are named per check in the table of item 24 |
| 2 | the record's literal `operation`, `predicate_type`, `provider.id`, `provider.version`, `evidence_id` and the shape test on it | the item-1 transcript | `operation inspect_web_page`, `predicate_type rea.web-page-inspection`, `provider.id rea-cdp-browser`, `provider.version 2`, `evidence_id ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd`, `evidence_id.shape True` | the record's own fields; the shape test is the script's literal regex |
| 3 | the target type, url, origin and title, the frame url, the dom-url set, the script count, the resource count, the resource's type, mime type and content size, and the two reconciliation statuses | the item-2 transcript | `target.type page`, `target.url http://127.0.0.1:8477/index.html`, `target.origin http://127.0.0.1:8477`, `target.title r77 probe page [loaded]`, `frames[0].url http://127.0.0.1:8477/index.html`, `metadata.dom_urls [{"node_index": 10, "attribute": "src", "url": "http://127.0.0.1:8477/app.js", "destination_scope": "approved"}]`, `scripts.total 2`, `resources count 1`, `resource Script text/javascript 101 http://127.0.0.1:8477/app.js`, `app.js script reconciliation exact`, `inline script reconciliation unmatched` | the record's own fields; the derived expectations they meet are the oracle's, named in item 1's row |
| 4 | the two fixture files' byte lengths and the record's two script lengths and script urls | the item-3 transcript | `index.html byte length 316`, `app.js byte length 101`, `record scripts.total 2`, `record script lengths [46, 101]`, `record script urls ['http://127.0.0.1:8477/app.js', 'http://127.0.0.1:8477/index.html']` | the file lengths are measured over the committed bytes; the record's lengths are the record's own fields, and the oracle compares the two |
| 5 | both `cdp_hash` values and the digests of the two authored script texts they equal | the item-4 transcript | `app.js byte length 101 sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`, `record app.js cdp_hash fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`, `app.js cdp_hash equals sha256(committed bytes) True`, `inline script text length 46 sha256 ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783`, `record inline cdp_hash ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783`, `inline cdp_hash equals sha256(inline text from index.html bytes) True` | the digests are computed over the committed bytes; the `cdp_hash` values are the record's own fields |
| 6 | the record file's byte length and digest, the receipt's recorded `stdout_sha256`, `exit_code`, `duration_seconds` and `producer` string, and the two fixture digests | the item-5 transcript | `inspection.json byte length 10816`, `inspection.json sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`, `receipt.stdout_sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`, `record sha256 equals receipt stdout_sha256 True`, `receipt.exit_code 0`, `receipt.duration_seconds 3.498`, `receipt.producer rea 6.8.0 (installed CLI; provider rea-cdp-browser, built-in; browser surface is the host's own Chrome/156.0.8078.74 headless on loopback CDP — no engine installed or updated)`, `index.html sha256 46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45`, `app.js sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593` | the digests are computed over the committed bytes; the four `receipt.*` values are the saved receipt's own recorded fields |
| 7 | the volatile field list | the item-6 transcript | the five entries of the `volatile_not_compared` array, printed as the seven lines of the `json.dumps(..., indent=1)` output | the authored premise file's own list |
| 8 | the capture window, the completeness status, the browser product string and the record's `confidence` and `authority` | the item-6 transcript | `capture_window {"started_at": "2026-11-01T06:59:28.999Z", "ended_at": "2026-11-01T06:59:29.701Z", "observation_ms": 500}`, `completeness.status policy_filtered`, `browser.product Chrome/156.0.8078.74`, `record confidence observed authority external-service` | the record's own recorded fields |

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | every load-bearing fact about the record and the fixture rests on S495, the lane's own tier-A record row opened this round (2026-11-05) whose anchors are the saved record's stdout digest, the receipt's recorded exit code and the two fixture digests; the one external sentence rests on S496, a tier-A docs row opened this round whose located quote is the DevTools Protocol landing page's self-description. No tier-C row is cited and no claim rests on one. |
| Q02 | pass | the header carries `source:` (two registry rows with their anchors, URLs and opened date), `verified-at:` (the lane commit, the command that resolves it and the byte-identity clause), `recheck:` (one runnable command and the stdout line it must end with) and `coverage-map: C08` naming the row this entry fills. |
| Q03 | pass | every expectation is derived from the committed fixture bytes (the digests and lengths the oracle computes itself) or fixed outside the record under test (the authored premise file's pins and hypotheses); no expectation is copied out of the record being checked, and the reading rule in the Observation section and the table in item 24 name the side of each comparison. |
| Q04 | pass | the analysis is manual byte reading by the lane's own committed scripts; the entry credits those scripts only with the lines their own stdout prints, and the producer only with the literal fields of the saved record. |
| Q05 | n/a | the entry makes no readiness or capability claim: no producer was invoked, and the receipt fields that record the earlier round-77 run are labelled recorded, not re-verified as a live capability. |
| Q06 | pass | the fixture premises are byte-verified on every oracle run: the script re-hashes both fixture files and compares their lengths against the authored premise file before it compares anything else (the oracle's first two check lines). |
| Q07 | pass | no parser behaviour is predicted here; the expectation side of every oracle check is named in the table of item 24, and the recorded outcome is reported whichever way it fell. |
| Q08 | superseded | QUALITY.md Q11 supersedes Q08; Q11 below is the operative criterion. |
| Q09 | pass | every digest is claimed only for the bytes it hashed (item 11); no origin, completeness or authenticity claim is made, and the record-file digest comparison is labelled a byte-identity check (item 25). |
| Q10 | pass | the scope is one provider operation, one authored inert fixture and one saved record; no general Chrome, CDP, Electron or browser claim is made, and the external row is cited for its self-description only (items 19 and 20). |
| Q11 | pass | every count, identifier and digest above is carried by a named stdout line of a named command, and the table in the Provenance section names that line and the expectation side of it; the values that are only recorded are labelled recorded (items 1, 2, 3, 6 and the note under the table of item 24). |
| Q12 | n/a | the entry cites no rejected source row and makes no reject/flip claim. |
| Q13 | pass | the recheck command is credited only with re-deriving the numbers it prints; the clauses it cannot detect are named — deleting a clause, a table row or a sentence of this entry — and the one-liner transcripts are named as not re-executed by the embedded-output gate (items 26 and 27). |
| Q14 | pass | no prose hex run carries a byte count; the counted byte values are command output inside fenced blocks, not prose literals. |
| Q15 | pass | the one git object id in this entry, `02050cb2a6758e3bd9cec696ff0e42df6f23511a`, is named with the command that resolves it (`git rev-parse 02050cb2a6758e3bd9cec696ff0e42df6f23511a^{commit}`) in the `verified-at:` header line, and the corpus tree's byte-identity at that commit is stated with the command that shows it. |
| Q16 | pass | each coverage statement names only what the named command prints: the item blocks quote the commands' own stdout lines, the reading rule in the Observation section states which side each printed value comes from, and the Provenance table maps each statement to the line that carries it. The `ORACLE OK (17/17 checks)` summary line is credited only as the run's own count of its checks. |
| Q17 | pass | no cited artifact was relocated in this round; every path this entry names resolves in the tree at the stated commit. |

## Sources

- **S495** (own-work, tier A, opened 2026-11-05) — the lane's own saved round-77 CDP browser-runtime record and
  its authored fixture, `corpus/live/runs/round-77/` and `corpus/fixtures/browser-r77/`. Anchors: the saved producer
  stdout `corpus/live/runs/round-77/inspection.json` with its sha256, the saved receipt's recorded exit code, the
  saved `LEDGER.md` record entry, and the two fixture files' digests; the opening evidence is the r77 oracle re-run
  on 2026-11-05, ending `ORACLE OK (17/17 checks)`. Scope: what this one saved record states for this one authored
  fixture — the producer stdout bytes, the receipt and the fixture digests — and no general claim about Chrome, CDP,
  Electron or any other browser.
- **S496** (docs, tier A, opened 2026-11-05) — Chrome DevTools Protocol,
  <https://chromedevtools.github.io/devtools-protocol/>. Anchor: the landing-hero intro paragraph, second sentence;
  the page carries no `ms.date` marker, HTTP Last-Modified 2026-11-04, ETag `6aeab6b6-8a86`. Located quote used here
  (15 words): "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based
  browsers." Scope: the protocol's own self-description only — that CDP is the JSON-based protocol Chrome exposes so
  that clients can instrument, inspect, debug and profile pages. Not cited for a compatibility guarantee, not for
  third-party support, and not for anything about the lane's own fixture.

## Reproduce

From the lane root, with the lane's committed scripts and the committed fixture bytes (no producer, no browser, no
network, nothing written):


```
$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json
check ok: fixture index.html sha256+len match truth.json
check ok: fixture app.js sha256+len match truth.json
check ok: authored anchors derived from index.html bytes
check ok: operation == inspect_web_page
check ok: provider.id == rea-cdp-browser
check ok: evidence_id shape ev_<64hex>
check ok: target.url == http://127.0.0.1:8477/index.html
check ok: target.origin == http://127.0.0.1:8477
check ok: target.title == derived 'r77 probe page [loaded]'
check ok: target.type page and frames[0].url == page_url
check ok: metadata.dom_urls == exactly the app.js src
check ok: scripts.items count == 2 with page + app.js urls
check ok: app.js script length == 101 and reconciliation exact
check ok: inline script length == 46 (from index.html bytes)
check ok: app.js cdp_hash == sha256(committed app.js bytes)
check ok: inline script cdp_hash == sha256(inline text from index.html bytes)
check ok: resources == 1 app.js entry, content_size 101, text/javascript
ORACLE OK (17/17 checks)
```

Each command exits 0 and prints one line per check plus a summary line: `ORACLE OK (17/17 checks)`. The stdout line
count of the oracle block is 18.
