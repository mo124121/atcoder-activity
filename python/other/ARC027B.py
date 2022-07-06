N = int(input())
S1 = input()
S2 = input()

counters = {}


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


uf = UnionFind(255)

for i in range(10):
    uf.unite(0, ord(str(i)))

for i in range(N):
    uf.unite(ord(S2[i]), ord(S1[i]))

ret = 1
if not uf.same(ord(S1[0]), 0):
    ret = 9
    uf.unite(0, ord(S1[0]))

for i in range(1, N):
    if not uf.same(0, ord(S1[i])):
        ret *= 10
        uf.unite(0, ord(S1[i]))

print(ret)
