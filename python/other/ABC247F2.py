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


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
MOD = 998244353

uf = UnionFind(N + 1)
for p, q in zip(P, Q):
    uf.unite(p, q)

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp2 = [[0] * 2 for _ in range(N + 1)]
dp2[0][1] = 1
memo = [0] * (N + 1)
for i in range(N):
    dp[i + 1][0] = dp[i][1] % MOD
    dp[i + 1][1] = (dp[i][0] + dp[i][1]) % MOD
    dp2[i + 1][0] = dp2[i][1] % MOD
    dp2[i + 1][1] = (dp2[i][0] + dp2[i][1]) % MOD
    memo[i + 1] = (dp[i + 1][0] + dp2[i + 1][1]) % MOD

count = Counter()
for i in range(1, N + 1):
    count[uf.root(i)] += 1

ret = 1
for v in count.values():
    ret *= memo[v]
    ret %= MOD
print(ret)
