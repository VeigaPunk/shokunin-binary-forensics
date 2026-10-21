import hashlib, json
F = ['subject','provider','analysis_profile','predicate_type','operation','parameters',
     'raw_result','normalized_result','confidence','authority','environment','limitations',
     'locations','evidence_links']
def canon(o):
    return json.dumps(o, sort_keys=True, separators=(',',':'), ensure_ascii=False).encode()
for r in (19,21,22,23,24,25,26):
    rec = json.load(open(f'corpus/live/runs/round-{r}/inspection.json'))
    proj = {k: rec[k] for k in F}
    proj['subject'] = {k: rec['subject'][k] for k in ('digest','format','architecture')}
    got = 'ev_'+hashlib.sha256(canon(proj)).hexdigest()
    print(f'r{r} recorded={rec["evidence_id"]} match={got == rec["evidence_id"]}')
