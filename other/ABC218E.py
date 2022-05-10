N, M = map(int, input().split())
from collections import defaultdict
from heapq import heappop, heappush

G = defaultdict(list)
C = [0] * (M + 1)
for i in range(1, M + 1):
    a, b, c = map(int, input().split())
    G[a].append((c, b, i))
    G[b].append((c, a, i))
    C[i] = c

h = []
c = 0
heappush(h, (c, 1, 0))
seen = set()
while len(h):
    c, node, edge = heappop(h)
    if node in seen:
        continue
    C[edge] = 0
    seen.add(node)
    for c_i, nxt, edge in G[node]:
        if nxt not in seen:
            heappush(h, (c + c_i, nxt, edge))
print(sum(C))
"""
見るからに最小費用流
いや違うか

単純にダイクストラして、
使わない接続辺のコスト合計

はい違います、クラスカル法
しかしなぜだめなのか？

"""
