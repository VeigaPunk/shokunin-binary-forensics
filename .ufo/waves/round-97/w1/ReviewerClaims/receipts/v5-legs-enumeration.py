import re
t = open("/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-96/c1_k_admit_counter5.py").read()
legs = set(re.findall(r'legs\["(C1_[A-Z0-9_]+)"\]', t))
print(len(legs), sorted(legs))
