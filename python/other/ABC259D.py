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


N = int(input())

sx, sy, tx, ty = map(int, input().split())

uf = UnionFind(N + 2)  # +2はsとt

XYR = []
for i in range(N):
    x, y, r = map(int, input().split())
    XYR.append((x, y, r))


for i in range(N):
    x1, y1, r1 = XYR[i]
    if (sx - x1) ** 2 + (sy - y1) ** 2 == r1**2:
        uf.unite(N, i)
    if (tx - x1) ** 2 + (ty - y1) ** 2 == r1**2:
        uf.unite(N + 1, i)
    for j in range(i, N):
        x2, y2, r2 = XYR[j]
        d = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if (r1 - r2) ** 2 <= d <= (r1 + r2) ** 2:
            uf.unite(i, j)

if uf.same(N, N + 1):
    print("Yes")
else:
    print("No")
