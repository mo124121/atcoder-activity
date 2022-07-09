#!/usr/bin/env python3
import sys


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


def solve(W: int, N: int, L: "List[int]", R: "List[int]"):
    ret = []
    lst = LazySegmentTree(W)
    for i in range(N):
        highest = lst.query(L[i] - 1, R[i])
        lst.update(L[i] - 1, R[i], highest + 1)
        ret.append(highest + 1)
    print(*ret, sep="\n")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(W, N, L, R)


if __name__ == "__main__":
    main()