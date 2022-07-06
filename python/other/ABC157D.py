from collections import Counter, defaultdict
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
        if root_x == root_y:
            return
        else:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


N, M, K = map(int, input().split())
uf = UnionFind(N + 1)

A = [0] * M
B = [0] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    uf.unite(A[i], B[i])
C = [0] * K
D = [0] * K
for i in range(K):
    C[i], D[i] = map(int, input().split())

count = Counter()
for i in range(1, N + 1):
    count[uf.root(i)] += 1

ret = [0] * (N + 1)
for i in range(1, N + 1):
    ret[i] = count[uf.root(i)] - 1

for a, b in zip(A, B):
    if uf.same(a, b):
        ret[a] -= 1
        ret[b] -= 1
for c, d in zip(C, D):
    if uf.same(c, d):
        ret[c] -= 1
        ret[d] -= 1

print(*ret[1:])


"""
だれか仲介がいるイメージ
友達の友達は友達候補

ある種の連結性を考える
UFで連結を生成
その中で組み合わせられる全パターンのうち、
友達orブロックのパターンを差し引く

それぞれの候補だすことを考えてなかった

AC
振り返ると最後の通し方はだいぶ雰囲気
各rootで連結の大きさをとる→各ノードの候補数を求める→対象外であるものを削る
"""
