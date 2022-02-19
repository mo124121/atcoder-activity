#!/usr/bin/env python3
from collections import defaultdict
import sys


class SegmentTree:
    def __init__(self, N, INF=-1) -> None:
        n = 1
        while n < N:
            n <<= 1

        self.n = n
        self.INF = INF
        self.elements = [INF] * (2 * n - 1)

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

    def query(self, a, b):
        return self._query_rec(a, b, 0, 0, self.n)

    def _query_rec(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.INF
        elif a <= l and r <= b:
            return self.elements[k]
        else:
            vl = self._query_rec(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self._query_rec(a, b, k * 2 + 2, (l + r) // 2, r)
            return max(vl, vr)

    def show(self):
        ret = []
        for i in range(self.n, self.n * 2 - 1):
            if self.elements[i] != self.INF:
                ret.append(((i - self.n + 1), self.elements[i]))
        print(*ret)


def solve(W: int, N: int, L: "List[int]", R: "List[int]", V: "List[int]"):
    st = SegmentTree(W + 1, INF=0)
    st.update(0, 0)
    nl = [-1] * (W + 1)
    nl[0] = 0

    for i in range(N):
        for j in range(L[i], R[i]):
            nl[j] = max(nl[j], st.query(0, j - L[i] + 1) + V[i])
        for j in range(R[i], W + 1):
            nl[j] = max(nl[j], st.query(j - R[i], j - L[i] + 1) + V[i])

        st.update_range(0, W + 1, nl)
        print(i, end=" ")
        st.show()

    ret = st.query(W, W + 1)
    print(ret)

    return


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
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(W, N, L, R, V)


if __name__ == "__main__":
    main()

"""
考察
・消費量の範囲・・？なんかきな臭い

・基本L[i]での貪欲法？ただ、何かの問題解説で貪欲法だとうまくいかなくてdpみたいなのを読んだ気もする
・すごいナップサック問題くさい、つまりdp？
・基本はdpしつつ、何らかの形で消費量の幅みたいなものを確保できるようにしたい->範囲？つまりセグ木？んなことある？
・Wが10000、Nが500->これでdpしたくなる　WxN的な？
・dpといもす複合とかもいいのかも、うまく伝播できるかな？->やってみる
dp[i+1][j]=i+1番目までの料理でつかうj mg香辛料（いもす記載）を使った時の価値

うまくいかない
冷静に考えると範囲のフラグを使っていもす的でいいのでは？
->買わなかったときの範囲が指定できなくない？やっぱdpでは？

いもすは都度展開すべきな気がする

冷静に考えると個数無制限のナップサック問題な気がする
選ばなかったときの遷移
選んだ時の遷移　いやでも範囲なのがしんどい

dp x セグ木か？
N x W x logW　でいける？

"""
