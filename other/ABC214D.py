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


N = int(input())

WUV = []
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    WUV.append((w, u, v))

WUV.sort()

uf = UnionFind(N + 1)

ans = 0
for w, u, v in WUV:
    ans += w * uf.size(u) * uf.size(v)
    uf.unite(u, v)

print(ans)


"""
解説読む
主客転倒の発想がなかった

最大値の合計->小さい方からuf等でつなげていって順次計算する
"""
