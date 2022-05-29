from collections import Counter
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


from functools import lru_cache


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 998244353


@lru_cache(maxsize=None)
def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x % MOD


ufw = UnionFind(N)
ufh = UnionFind(N)

for h1 in range(N - 1):
    for h2 in range(h1 + 1, N):
        flag = True
        for w in range(N):
            if A[h1][w] + A[h2][w] > K:
                flag = False
                break
        if flag:
            ufh.unite(h1, h2)
for w1 in range(N - 1):
    for w2 in range(w1 + 1, N):
        flag = True
        for h in range(N):
            if A[h][w1] + A[h][w2] > K:
                flag = False
                break
        if flag:
            ufw.unite(w1, w2)

cw = Counter()
ch = Counter()
for i in range(N):
    cw[ufw.root(i)] += 1
    ch[ufh.root(i)] += 1

ret = 1
for v in list(cw.values()) + list(ch.values()):
    ret *= factorial(v)
    ret %= MOD


print(ret)


"""
交換できる行をufで管理していく
連結成分毎にfactorial

"""
