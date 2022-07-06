Q = int(input())
ret = []
N = 2**20
A = [-1] * (N)


class UnionFindLike:
    def __init__(self, N) -> None:
        self.parent = [i for i in range(N)]

    def root(self, i):
        if i == self.parent[i]:
            return i
        j = self.root(self.parent[i])
        if j != self.parent[i]:
            self.parent[i] = j
        return j

    def same(self, x, y):
        return self.parent[x] == self.parent[y]

    def unite(self, x, y):
        if not self.same(x, y):
            self.parent[x] = y


ufl = UnionFindLike(N)

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = ufl.root(x % N)
        A[h] = x
        ufl.unite(h, (h + 1) % N)
    if t == 2:
        ret.append(A[x % N])
print(*ret, sep="\n")

"""
N=2**20->10**6
bisectや

んーなんか違う
同じやつを刺された時のポインタみたいなのが欲しい 一番右はこいつ、的な

bisectでできてる気がするが、
16WA/18
結構根本的に間違えている？

解説後　根本的に間違えていた
UFで実装すべき

"""
