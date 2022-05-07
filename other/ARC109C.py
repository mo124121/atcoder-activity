import sys

sys.setrecursionlimit(10**6)
# import pypyjit
# pypyjit.set_param("max_unroll_recursion=-1")

N, K = map(int, input().split())
S = input()

win = {
    ("R", "S"): "R",
    ("S", "R"): "R",
    ("R", "P"): "P",
    ("P", "R"): "P",
    ("P", "S"): "S",
    ("S", "P"): "S",
}


def rec(l, r):
    if r - l == 1:
        return S[l % N]
    m = (l + r) // 2
    L = rec(l, m)
    R = rec(m, r)
    if L == R:
        return L
    return win[(L, R)]


print(rec(0, 2**K))


"""
分割統治っぽい
ソートアルゴの改変に見える


2**100はでかいので、やり方に工夫が必要
多倍長でぶち込んでもいいがどうか
一回やってみる

無理そうなら外部リストなりなんなり作って管理する

多倍長では間に合いそうだが16WA/26
2**Kじゃなくて2*Kにしてた
そして間に合わない

さてどう圧縮するか？

mod上で同じスタート・同じ人数なら結果は同じ　これを使えないか？

"""
