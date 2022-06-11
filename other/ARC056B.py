import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


class UnionFind:
    def __init__(self, N):

        self.parent = [0] * N
        self.rank = [0] * N
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
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


N, M, S = map(int, input().split())
from collections import defaultdict

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

uf = UnionFind(N + 1)
ret = []
for i in range(N, 0, -1):
    for nxt in G[i]:
        if nxt > i:
            uf.unite(nxt, i)
    if uf.same(i, S):
        ret.append(i)
print(*ret[::-1], sep="\n")


"""
逆の番号から連結していく
その時点で関係 Sとufで繋がっていればよい
"""
