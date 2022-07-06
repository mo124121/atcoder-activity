N, M = map(int, input().split())
from collections import defaultdict, deque

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def dk(start, G):
    q = deque()
    q.append(start)
    d = [-1] * (N + 1)
    d[start] = 0
    while q:
        node = q.popleft()
        for nxt in G[node]:
            if d[nxt] < 0:
                d[nxt] = d[node] + 1
                q.append(nxt)
    return d


d1 = dk(1, G)
dN = dk(N, G)
ret = []
INF = 10**7
for i in range(1, N + 1):
    r = INF
    if d1[N] != -1:
        r = min(r, d1[N])
    if d1[0] != -1 and dN[i] != -1:
        r = min(r, d1[0] + dN[i])
    if d1[i] != -1 and dN[0] != -1:
        r = min(r, d1[i] + dN[0])
    if r == INF:
        r = -1
    ret.append(r)
print(*ret)
