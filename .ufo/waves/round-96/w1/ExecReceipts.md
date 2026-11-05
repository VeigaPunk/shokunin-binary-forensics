# Executed verification — round-96 quote receipts S502 / S503 (ExecReceipts)

Seat: ExecReceipts. Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin.
Method: read-only checks against the committed r96 receipts (fee4674367 feed freeze commit ff767436feed32cf2f4074f05f938f8cea98e69a as a notional commit).
Every Python invocation used `python3 -B`.

## 1) sha256 of raw bodies vs receipt fetch_sha256

```
$ sha256sum reports/round-96/quote-receipts/raw/S502.body reports/round-96/quote-receipts/raw/S503.body
c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24  reports/round-96/quote-receipts/raw/S502.body
b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc  reports/round-96/quote-receipts/raw/S503.body
```

Receipt `fetch_sha256` fields (jq-style extraction via python3 -B json load):

```
S502 c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24
S503 b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc
```

Both match the task-quoted expected values byte-for-byte, and the body byte sizes match the receipts'
`length` fields (S502 38167, S503 35095; `wc -c` output 38167 / 35095 / total 73262).

## 2) audit_source_quotes verify (lane root)

```
$ PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-96/quote-receipts --sid S502 --sid S503
S502 terminal=S502 state=verified (ok)
S503 terminal=S503 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
EXIT=0
```

Exit 0 and SUMMARY rows=2 verified=2 as expected.

## 3) fetch-log.md one line per sid; quote word counts

`grep` for each sha256 in fetch-log.md returns one bullet per sid (S502 line and S503 line), each naming
the sid and its sha256; the same two bullet lines carry the pinned URLs and byte counts. The 404 probe
line is disclosed as not appended (no row for a 404), matching the receipt set of two.

Quote word counts (python3 -B, quote strings from the receipt JSONs):

```
S502: words=12 (<=25: True) quote='rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally'
S503: words=17 (<=25: True) quote='Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction.'
```

Both <= 25.

## 4) URL host + pinned revision

Parsed `fetch_url` from each receipt (urllib.parse):

```
S502: host=raw.githubusercontent.com host_ok=True rev_ok=True (12f6e0974cc0db0b3a9b86246accc76556837222 present)
S503: host=raw.githubusercontent.com host_ok=True rev_ok=True (12f6e0974cc0db0b3a9b86246accc76556837222 present)
```

`grep -o` counts on fetch-log.md: `raw.githubusercontent.com` x2, `12f6e0974cc0db0b3a9b86246accc76556837222` x2 — host and revision appear in both bullet lines.

## 5) raw-byte quote presence (beyond the assigned four, v4-leg sanity)

```
S502: span={'start': 26309, 'end': 26411} len(slice)=102 len(quote_utf8)=102 quote_bytes_in_raw=True quote_equals_slice=False
S503: span={'start': 257, 'end': 389} len(slice)=132 len(quote_utf8)=132 quote_bytes_in_raw=True quote_equals_slice=True
```

S503 slice equals the quote byte-for-byte. S502 first diff at offset 0: slice=` ` quote=`r`; both
strings are 102 bytes; the quote bytes occur in the raw body at offset 26310 (` quote_bytes_in_raw=True`),
so the committed span is off by one leading space but the quote is genuinely pinned to the body bytes.

## 6) candidate digest re-derive (context)

```
2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923
```

Matches the frozen candidate digest.

## Verdict

All four assigned checks PASS. Chain holds: bodies hash to the receipt sha256 fields, the audit ledger
verifies both rows, the fetch log names each sid with its sha256, quotes are <=25 words, URLs are on
raw.githubusercontent.com at pinned revision 12f6e0974cc0db0b3a9b86246accc76556837222.
