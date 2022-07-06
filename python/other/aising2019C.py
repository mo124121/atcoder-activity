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


H, W = map(int, input().split())
S = [input() for _ in range(H)]

mvs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

uf = UnionFind(H * W)

for h in range(H):
    for w in range(W):
        for hm, wm in mvs:
            hn = h + hm
            wn = w + wm
            if 0 <= hn < H and 0 <= wn < W and S[h][w] != S[hn][wn]:
                uf.unite(h * W + w, hn * W + wn)

count_bk = Counter()
count_wh = Counter()
for h in range(H):
    for w in range(W):
        r = uf.root(h * W + w)
        if S[h][w] == "#":
            count_bk[r] += 1
        else:
            count_wh[r] += 1

ret = 0
for k, vb in count_bk.items():
    ret += vb * count_wh[k]

print(ret)


"""
ufで白黒が隣あう要素を管理して、つながりの有無を考える
黒黒となる場合はほかの経路でも白黒ではいけないはず
"""
