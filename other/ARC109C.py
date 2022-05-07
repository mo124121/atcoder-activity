N, K = map(int, input().split())
S = input()

win = {
    ("R", "S"): "R",
    ("S", "R"): "R",
    ("R", "R"): "R",
    ("R", "P"): "P",
    ("P", "R"): "P",
    ("P", "P"): "P",
    ("P", "S"): "S",
    ("S", "P"): "S",
    ("S", "S"): "S",
}

memo = [[""] * (N) for _ in range(K + 1)]
for i in range(N):
    memo[0][i] = S[i]
for i in range(K):
    for j in range(N):
        l = memo[i][j]
        r = memo[i][(j + pow(2, i, N)) % N]
        memo[i + 1][j] = win[(l, r)]


print(memo[K][0])


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
先に保存しておく
memo[K][N]

すったもんだでAC


"""
