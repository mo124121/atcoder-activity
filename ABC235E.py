from bisect import bisect_left


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

    def check_renketsu(self):
        root = self.root(0)
        for i in range(1, len(self.parent)):
            if root != self.root(i):
                return False
        return True


N, M, Q = map(int, input().split())

a = [0] * M
b = [0] * M
c = [0] * M

for i in range(M):
    a[i], b[i], c[i] = map(int, input().split())
edges = [(c[i], a[i], b[i]) for i in range(M)]
edges.sort()
a = [edges[i][1] for i in range(M)]
b = [edges[i][2] for i in range(M)]
c = [edges[i][0] for i in range(M)]

u = [0] * Q
v = [0] * Q
w = [0] * Q
for i in range(Q):
    u[i], v[i], w[i] = map(int, input().split())
edges = [(w[i], u[i], v[i]) for i in range(M)]
edges.sort()
u = [edges[i][1] for i in range(M)]
v = [edges[i][2] for i in range(M)]
w = [edges[i][0] for i in range(M)]

for i in range(Q):
    J = bisect_left(c, w[i])
    uf = UnionFind(N)
    for j in range(J):
        uf.unite(a[j] - 1, b[j] - 1)
    if uf.same(u[i] - 1, v[i] - 1) or uf.check_renketsu():
        print("No")
    else:
        print("Yes")
