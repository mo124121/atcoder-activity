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


N, M, Q = map(int, input().split())

edges = []

for i in range(M + Q):
    u, v, w = map(int, input().split())
    edges.append((w, u, v, len(edges)))

edges.sort()

uf = UnionFind(N)
ret = [None] * Q
for e in edges:
    w, u, v, i = e
    if i >= M:
        if uf.same(u - 1, v - 1):
            ret[i - M] = "No"
        else:
            ret[i - M] = "Yes"
    else:
        uf.unite(u - 1, v - 1)

print(*ret, sep="\n")
