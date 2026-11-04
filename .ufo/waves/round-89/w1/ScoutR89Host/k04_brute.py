import itertools, sys
sys.path.insert(0, "/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus")
import importlib.util
spec = importlib.util.spec_from_file_location("cr", "/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/census_reprobe.py")
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)

def score(text):
    t = text.lower()
    n = 0
    for (kind, arg) in [("presence","ghidra"), ("presence","ida")]:
        k, a, tokens, forbidden = cr.live((kind, arg))
        if any(tok.lower() not in t for tok in tokens):
            n += 1
        elif any(w.lower() in t for w in forbidden):
            n += 1
    return n

# vocabulary sweep over polarity words
words = ["present","absent","installed","not installed","missing","available","unavailable",
         "Present","ABSENT","present.","absent;","xpresentx","xabsentx","present-","absent-",
         "re-","none","no","yes","0 of 2","1 of 2","2 of 2","on PATH","off PATH","found","gone"]
best = 99; argbest=None
for a in words:
    for b in words:
        for tmpl in ["{a}, {b}", "{a} {b}", "ghidra {a}; ida {b}", "ida {b}; ghidra {a}"]:
            text = tmpl.format(a=a, b=b)
            s = score(text)
            if s < best:
                best, argbest = s, text
print("min K04 mismatches over", len(words)**2*4, "candidates:", best)
print("example:", repr(argbest))
# exhaustive over the raw polarity pair
for a,b in [("present","absent"),("absent","present"),("present","present"),("absent","absent")]:
    print(repr(a+b), "->", score(f"{a}, {b}"))
