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

A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

ret = 0
for i in range(M):
    uf = UnionFind(N + 1)
    for j in range(M):
        if i == j:
            continue
        uf.unite(A[j], B[j])
    if not uf.same(A[i], B[i]):
        ret += 1
print(ret)

"""
M<50

とりあえずi番目の辺を除く要素をufでくっつけて、
除いた要素同士がnot sameの場合は数える

AC
ただ、lowlink O(V+E)も知っておこう
"""
