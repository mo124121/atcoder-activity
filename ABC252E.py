from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c, i + 1))
    G[b].append((a, c, i + 1))

h = []
d = 0
node = 1
e = 0
parent = 0
heappush(h, (d, node))
ret = [-1] * (N + 1)
INF = 10**18
dist = [INF] * (N + 1)

while h:
    d, node = heappop(h)

    if dist[node] < d:
        continue

    for nxt, c, e in G[node]:
        nd = d + c
        if dist[nxt] > nd:
            dist[nxt] = nd
            ret[nxt] = e
            heappush(h, (nd, nxt))

print(*ret[2:])

"""
最小全域木でいいか？
1からの積算コストで作ればok
あーでもポテンシャルとかありそうなんだよなあ

"""
