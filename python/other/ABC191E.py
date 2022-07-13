N, M = map(int, input().split())

from collections import defaultdict
from heapq import heappop, heappush

G = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))


INF = 10**18
for i in range(1, N + 1):
    h = []

    for b, c in G[i]:
        heappush(h, (c, b))

    dist = [INF] * (N + 1)
    while h:
        d, a = heappop(h)
        if dist[a] != INF:
            continue
        dist[a] = d
        if a == i:
            break
        for b, c in G[a]:
            heappush(h, (d + c, b))

    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])
