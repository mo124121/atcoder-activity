N, M = map(int, input().split())
from collections import defaultdict
from itertools import product

G = defaultdict(set)
for i in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
ret = 0
for p in product((True, False), repeat=N):
    flag = True
    r = 0
    for i, m1 in enumerate(p):
        if not m1:
            continue
        r += 1
        for j, m2 in enumerate(p):
            if i == j:
                continue
            if m2:
                if not i + 1 in G[j + 1]:
                    flag = False
                    break
    if flag:
        ret = max(ret, r)
print(ret)
