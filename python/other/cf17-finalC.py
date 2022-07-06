from itertools import product


N = int(input())
D = list(map(int, input().split()))
MAX_SIZE = 13

ret = 0
Ds = set()
for pat in product((False, True), repeat=min(MAX_SIZE, N)):
    seen = set([0])
    r = 12
    for i, p in enumerate(pat):
        if p:
            t = 24 - D[i]
        else:
            t = D[i]
        for v in seen:
            t2 = abs(t - v)
            r = min(r, t2, 24 - t2)
        seen.add(t)
    if ret < r:
        ret = max(ret, r)
        Ds = seen

if N > MAX_SIZE:
    for d in D[MAX_SIZE:]:
        if d not in Ds:
            Ds.add(d)
        elif -d not in Ds:
            Ds.add(-d)
        else:
            ret = 0
            break

print(ret)
