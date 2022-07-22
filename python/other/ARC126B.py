from bisect import bisect, bisect_left
from collections import defaultdict

N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
INF = 10**10
ret = [INF] * (N + 1)
for i in range(1, N + 1):
    G[i].sort(reverse=True)
    for nxt in G[i]:
        ret[bisect_left(ret, nxt)] = nxt

print(bisect_left(ret, INF))
