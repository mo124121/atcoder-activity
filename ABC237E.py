N, M = map(int, input().split())
H = [0] + list(map(int, input().split()))
# scoreは反転
WORST = 2 * 10 ** 8

from collections import defaultdict

G = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    diff = H[u] - H[v]
    if diff > 0:
        G[u].append((v, 0))
        G[v].append((u, diff))
    else:
        G[u].append((v, -diff))
        G[v].append((u, 0))

import heapq

h = []
heapq.heappush(h, (0, 1))


ret = 0
dist = [WORST + H[i] for i in range(N + 1)]
while len(h):
    d, hiroba = heapq.heappop(h)
    if dist[hiroba] < d:
        continue
    ret = min(d + H[hiroba] - H[1], ret)
    best_hiroba = 0
    for neibor, cost in G[hiroba]:
        if dist[neibor] > d + cost:
            dist[neibor] = d + cost
            heapq.heappush(h, (d + cost, neibor))
print(-ret)
