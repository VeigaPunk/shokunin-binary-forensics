#!/usr/bin/env python3
"""S092 quarantine hand-check: re-derive register absence claim for
http://cjc.ict.ac.cn/online/bfpub/yyc-2020818141436.pdf (fetched bytes in ./source.bin)."""
import hashlib, html, os, shutil, subprocess, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, 'source.bin')
data = open(PATH, 'rb').read()
print(f'bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}')

A = '计 算 机 学 报 / 2020 CHINESE JOURNAL OF COMPUTERS / 嵌入式设备固件安全分析技术研究综述 / 于颖超 1) 陈左宁 2) 甘水滔 1) 秦晓军 1) / 1) (数学工程与先进计算国家重点实验室，江'
B = '从静态分析、符号执行、模糊测试、程序验证、基于机器学习的方法等角度综述了现有固件缺陷检测方法'

def variants(s):
    return [('as-is', s), ('html.escape', html.escape(s)),
            ('html.unescape', html.unescape(s)),
            ('numeric-entities', ''.join(f'&#{ord(c)};' if ord(c) > 127 else c for c in s))]

encs = ['utf-8', 'utf-16-le', 'utf-16-be', 'gb18030', 'big5']
print('== RAW BYTE SEARCH (fixed-string, case-sensitive) ==')
raw_hits = 0
for nm, s0 in [('A', A), ('B', B)]:
    for vlabel, sv in variants(s0):
        for enc in encs:
            try:
                needle = sv.encode(enc, errors='strict')
            except Exception:
                continue
            i = data.find(needle)
            if i >= 0:
                raw_hits += 1
                print(f'HIT {nm} variant={vlabel} enc={enc} offset={i}')
print('raw hits:', raw_hits if raw_hits else 'NONE')

frags = ['嵌入式设备固件', '固件安全分析技术研究综述', '固件安全', '于颖超', '陈左宁', '甘水滔',
         '秦晓军', 'CHINESE JOURNAL OF COMPUTERS', '从静态分析', '符号执行', '模糊测试',
         '程序验证', '基于机器学习', '固件缺陷检测', '数学工程与先进计算']
print('== RAW FRAGMENT NET (per-encoding counts) ==')
for f in frags:
    enc_hit = []
    for enc in encs:
        try:
            n = f.encode(enc)
        except Exception:
            continue
        cnt = data.count(n)
        if cnt:
            enc_hit.append((enc, cnt, data.find(n)))
    print(f'{f}: {enc_hit if enc_hit else "absent-in-raw"}')

print('== TEXT EXTRACTION ==')
text, how = None, ''
pdftotext = shutil.which('pdftotext')
if pdftotext:
    out = os.path.join(HERE, 'extracted.txt')
    r = subprocess.run([pdftotext, '-enc', 'UTF-8', '-layout', PATH, out],
                       capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 0:
        text = open(out, encoding='utf-8', errors='replace').read()
        how = f'pdftotext({pdftotext}) -layout, {len(text)} chars'
if text is None:
    try:
        import pypdf  # noqa
        from pypdf import PdfReader
        rd = PdfReader(PATH)
        text = '\n'.join((pg.extract_text() or '') for pg in rd.pages)
        how = f'pypdf {pypdf.__version__}, {len(text)} chars'
    except Exception as e:
        how = f'pypdf failed: {e}'
        try:
            from pdfminer.high_level import extract_text
            text = extract_text(PATH)
            how += f' | pdfminer, {len(text)} chars'
        except Exception as e2:
            how += f' | pdfminer failed: {e2}'
print('extractor:', how)
if not text:
    print('NO TEXT EXTRACTED'); sys.exit(0)

open(os.path.join(HERE, 'extracted.txt'), 'w', encoding='utf-8').write(text)
print('== EXTRACTED-TEXT SEARCH ==')
def ctx(t, i, n=90):
    return t[max(0, i - n // 2):i].replace('\n', '⏎') + ' ⟦' + t[i:i + n].replace('\n', '⏎') + '⟧'
for nm, s0 in [('A', A), ('B', B)]:
    for vlabel, sv in variants(s0):
        i = text.find(sv)
        if i >= 0:
            print(f'HIT {nm} variant={vlabel} text-offset={i}: {ctx(text, i)}')
    # whitespace-collapsed comparison (PDF extractors insert spaces/newlines)
    flat = re.sub(r'\s+', '', text)
    flatn = re.sub(r'\s+', '', sv)
    j = flat.find(flatn)
    if j >= 0:
        print(f'HIT {nm} variant={vlabel} WHITESPACE-COLLAPSED flat-offset={j}: ⟦{flat[max(0,j-45):j+len(flatn)+45]}⟧')
print('== EXTRACTED FRAGMENT NET ==')
for f in frags:
    fn = re.sub(r'\s+', '', f)
    i = text.find(f)
    k = re.sub(r'\s+', '', text).find(fn)
    if i >= 0:
        print(f'{f}: exact text-offset={i}: {ctx(text, i, 120)}')
    elif k >= 0:
        flat = re.sub(r'\s+', '', text)
        print(f'{f}: whitespace-collapsed flat-offset={k}: ⟦{flat[max(0,k-50):k+len(fn)+50]}⟧')
    else:
        print(f'{f}: absent')
