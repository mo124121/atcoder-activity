from collections import Counter
import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


class UnionFind:
    def __init__(self, N):

        self.parent_or_size = [-1] * N

    def root(self, x):
        if self.parent_or_size[x] < 0:
            return x
        else:
            self.parent_or_size[x] = self.root(self.parent_or_size[x])
            return self.parent_or_size[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if -self.parent_or_size[root_x] < -self.parent_or_size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent_or_size[root_x] += self.parent_or_size[root_y]
        self.parent_or_size[root_y] = root_x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent_or_size[self.root(x)]


N, M = map(int, input().split())


G = []
for i in range(M):
    a, b = map(int, input().split())
    G.append((a, b))

ret = []

G.reverse()
count = Counter()
count[1] = N
r = N * (N - 1) // 2
uf = UnionFind(N + 1)
for a, b in G:
    ret.append(r)
    if not uf.same(a, b):
        sa = uf.size(a)
        sb = uf.size(b)
        r -= sa * sb
        uf.unite(a, b)

print(*reversed(ret), sep="\n")
