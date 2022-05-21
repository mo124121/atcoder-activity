import sys

sys.setrecursionlimit(10**6)

from collections import defaultdict
from heapq import heappop, heappush

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")


class UnionFind:
    def __init__(self, N):

        self.parent = [0] * N
        for i in range(N):
            self.parent[i] = i

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        else:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


N, M = map(int, input().split())
G = defaultdict(list)
edge = [(0, 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c, i + 1))
    G[b].append((a, c, i + 1))
    edge.append((a, b))

uf = UnionFind(N + 1)

h = []
heappush(h, (0, 1, 0, 0))
ret = []
while h:
    d, node, e, parent = heappop(h)

    if uf.same(edge[e][0], edge[e][1]):
        continue

    uf.unite(edge[e][0], edge[e][1])
    ret.append(e)

    for nxt, c, en in G[node]:
        if nxt == parent or uf.same(nxt, node):
            continue
        heappush(h, (d + c, nxt, en, node))

print(*ret[1:])

"""
最小全域木でいいか？
1からの積算コストで作ればok
あーでもポテンシャルとかありそうなんだよなあ

"""
