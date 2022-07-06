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


# https://gist.github.com/masa-aa/4be96f053457dc60625a3552288fb1e4
class WeightedUnionFind:
    def __init__(self, N):
        N += 1
        self.par = [-1] * N
        self.diff_weight = [0] * N  # 根からの重み

    def root(self, x):
        q = []
        while self.par[x] >= 0:
            q.append(x)
            x = self.par[x]
        for i in reversed(q):
            self.diff_weight[i] += self.diff_weight[self.par[i]]
            self.par[i] = x

        return x

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y, w):
        x_root = self.root(x)
        y_root = self.root(y)
        w += self.diff_weight[x] - self.diff_weight[y]
        x, y = x_root, y_root
        if x == y:
            return
        if self.par[y] < self.par[x]:
            x, y, w = y, x, -w
        self.par[x] += self.par[y]
        self.par[y] = x
        self.diff_weight[y] = w


class SegmentTree:
    def __init__(self, N, init_value=-1, INF=-(10**15)) -> None:
        n = 1
        while n < N:
            n <<= 1

        self.n = n
        self.INF = INF
        self.elements = [init_value] * (2 * n - 1)

    def update(self, i, x):
        i += self.n - 1
        self.elements[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.elements[i] = max(self.elements[i * 2 + 1], self.elements[i * 2 + 2])

    def update_range(self, l, r, x):
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.n - 1
        r += self.n - 1
        self.elements[l:r] = x
        while 0 < l < r:
            l = (l - 1) // 2
            r = r // 2
            for i in range(l, r):
                self.elements[i] = max(
                    self.elements[i * 2 + 1], self.elements[i * 2 + 2]
                )

    def query(self, l, r):
        l += self.n - 1
        r += self.n - 1
        res = self.INF
        while l < r:
            res = max(max(res, self.elements[l]), self.elements[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res

    # 遅い
    # def query(self, a, b):
    #     return self._query_rec(a, b, 0, 0, self.n)

    # def _query_rec(self, a, b, k, l, r):
    #     if r <= a or b <= l:
    #         return self.INF
    #     elif a <= l and r <= b:
    #         return self.elements[k]
    #     else:
    #         vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
    #         vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
    #         return max(vl, vr)


class LazySegmentTree:
    def __init__(self, N, INF=0) -> None:
        n = 1
        while n < N:
            n *= 2

        self.n = n
        self.INF = INF
        self.elements = [INF] * (2 * n - 1)
        self.lazy = [INF] * (2 * n - 1)

    def eval(self, k):
        if self.lazy[k] == self.INF:
            return
        if k < self.n - 1:
            self.lazy[k * 2 + 1] = self.lazy[k]
            self.lazy[k * 2 + 2] = self.lazy[k]

        self.elements[k] = self.lazy[k]
        self.lazy[k] = self.INF

    def query(self, a, b):
        return self._query_rec(a, b, 0, 0, self.n)

    def _query_rec(self, a, b, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return self.INF
        elif a <= l and r <= b:
            return self.elements[k]
        else:
            vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
            return max(vl, vr)

    def update(self, a, b, x):
        self._update_rec(a, b, x, 0, 0, self.n)

    def _update_rec(self, a, b, x, k, l, r):
        self.eval(k)
        if r <= a or b <= l:
            return
        elif a <= l and r <= b:
            self.lazy[k] = x
            self.eval(k)
        else:
            self._update_rec(a, b, x, k * 2 + 1, l, (l + r) // 2)
            self._update_rec(a, b, x, k * 2 + 2, (l + r) // 2, r)
            self.elements[k] = max(self.elements[k * 2 + 1], self.elements[k * 2 + 2])
