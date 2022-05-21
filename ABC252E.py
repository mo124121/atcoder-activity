from collections import defaultdict
from heapq import heappop, heappush

N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c, i + 1))
    G[b].append((a, c, i + 1))

h = []
d = 0
node = 1
e = 0
parent = 0
heappush(h, (d, node, e, parent))
ret = []
seen = {}

while h:
    d, node, e, parent = heappop(h)

    if node in seen:
        continue
    seen[node] = d
    ret.append(e)

    for nxt, c, en in G[node]:
        if nxt != parent and nxt not in seen:
            heappush(h, (d + c, nxt, en, node))

print(*ret[1:])

"""
最小全域木でいいか？
1からの積算コストで作ればok
あーでもポテンシャルとかありそうなんだよなあ

"""
