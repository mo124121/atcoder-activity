from collections import defaultdict


N, M = map(int, input().split())
G = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)


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


uf = UnionFind(N + 1)
ret = [0]

seen = {N: True}
ind = {N: True}
r = 0
for i in range(N, 1, -1):
    r += 1
    for node in G[i]:
        if not uf.same(i, node):
            uf.unite(i, node)
            r -= 1

    ret.append(r)

print(*ret[::-1], sep="\n")
