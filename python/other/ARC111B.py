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


SIZE = 4 * 10**5
N = int(input())
uf = UnionFind(SIZE + 1)
E = []
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        uf.unite(0, a)
    else:
        E.append((a, b))

for a, b in E:
    if uf.same(a, b):
        uf.unite(0, a)
    uf.unite(a, b)

rs = set()
for i in range(SIZE + 1):
    rs.add(uf.root(i))

ret = 0
for r in rs:
    s = uf.size(r)
    if s != 1:
        ret += s - 1
print(ret)

"""

なんかすごいグラフっぽい

表裏同じのはさっさと使う
使ったやつを起点にグラフを辿っていく
次は1個のやつで辿る

そのあとはたぶん全部だせるんじゃね？わからん

unionfind＋αのほうが楽そう？別に繋がってる必要なない？
使用済みと繋がるイメージ

解説後
ufじゃなくても木か木じゃないかで＝サイクルを持つかで
連結成分を評価すればいい
"""
