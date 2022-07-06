from heapq import heappop, heappush
import sys

sys.setrecursionlimit(10**6)
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")


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
        if root_x != root_y:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


N, M = map(int, input().split())
h = []
for i in range(M):
    a, b, c = map(int, input().split())
    heappush(h, (c, a, b))

uf = UnionFind(N + 1)
ret = 0

while len(h):
    c, a, b = heappop(h)

    if c > 0 and uf.same(a, b):
        ret += c
    else:
        uf.unite(a, b)
print(ret)

"""
見るからに最小費用流
いや違うか

単純にダイクストラして、
使わない接続辺のコスト合計

はい違います、クラスカル法
しかしなぜダイクストラでだめなのか？


たぶんダイクストラがバグったのはマイナス辺があったからかも？


"""
