from collections import defaultdict


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


N, K, L = map(int, input().split())

uf1 = UnionFind(N + 1)

for i in range(K):
    p, q = map(int, input().split())
    uf1.unite(p, q)

uf2 = UnionFind(N + 1)

for i in range(L):
    r, s = map(int, input().split())
    uf2.unite(r, s)
sizes = defaultdict(int)

for i in range(1, N + 1):
    sizes[(uf1.root(i), uf2.root(i))] += 1

ret = []
for i in range(1, N + 1):
    ret.append(sizes[(uf1.root(i), uf2.root(i))])
print(*ret)

"""
ufくさい
グラフが連結か否か二つのグラフで

そのままやるとN**2で間に合わない

片方でufした後に、ついでにチェックしつつとか？

逆UF?なにそれ

片方でufして、ufじゃないものをつなぐ鉄道は追加しない
ufの大きさが答え

できてる気がするがWA
12/18WAで根本から違っているレベル
普通あり得る想定パターンが通っていない感覚か？

解説後AC

"""
