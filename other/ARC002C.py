N = int(input())
C = input()
ret = 10**3

COMS = "ABXY"

for a in COMS:
    for b in COMS:
        for c in COMS:
            for d in COMS:
                l = a + b
                r = c + d
                d = len(C.replace(l, "L").replace(r, "R"))
                ret = min(ret, d)
print(ret)
"""
N<1000
4**4=256パターン
全部やる
"""
