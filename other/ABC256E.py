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


N = int(input())
X = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

uf = UnionFind(N + 1)
ans = 0
for i in range(1, N + 1):
    if not uf.same(i, X[i]):
        uf.unite(i, X[i])
        continue

    s = X[i]
    r = C[i]
    while s != i:
        r = min(C[s], r)
        s = X[s]
    ans += r

print(ans)


"""
uf解への書き換え
"""
