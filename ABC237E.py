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
        G[u].append((v, -diff))
        G[v].append((u, 2 * diff))
    else:
        G[u].append((v, -2 * diff))
        G[v].append((u, diff))

import heapq
from collections import deque

h = []
heapq.heappush(h, (0, 1))
q = deque()


ret = 0
dist = [WORST] * (N + 1)
dist[0] = 0
while len(h):
    s, hiroba = heapq.heappop(h)
    if dist[hiroba] < s:
        continue
    ret = min(s, ret)
    best_hiroba = 0
    for neibor, cost in G[hiroba]:
        if dist[neibor] > s + cost:
            dist[neibor] = s + cost
            heapq.heappush(h, (s + cost, neibor))
print(-ret)
