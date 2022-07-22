N, M = map(int, input().split())
from collections import defaultdict, deque
from itertools import accumulate

A = []
B = []
G = defaultdict(list)
for i in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    A.append(a)

G2 = {}
for i in range(1, M + 1):
    if i in G:
        G2[i] = (min(G[i]), max(G[i]))
    else:
        G2[i] = (M, 1)


imos = [0] * (M + 2)
seen = set()

l = 1
mr = max(A)
ml = M + 1
for l in range(1, M + 1):
    if l > ml:
        break
    imos[mr - l + 1] += 1
    imos[M - l + 2] -= 1
    for nxt in G[l]:
        mr = max(mr, nxt)
        ml = min(ml, nxt)


ret = list(accumulate(imos))

print(*ret[1:-1])


"""
方針誤りなり

解説後
単調性に気づき、imos+尺取りを思いつくことが必要
"""
