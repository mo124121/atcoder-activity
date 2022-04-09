T = int(input())
for t in range(T):
    E, W = map(int, input().split())
    X = [[] for _ in range(E)]
    for e in range(E):
        X[e] = list(map(int, input().split()))

    ret = 0
    st = []
    for i in range(E):
        w_i = X[i][:]
        ret += sum(w_i) * 2
        for j in range(i, E):
            for w in range(W):
                w_i[w] = min(w_i[w], X[j][w])
                X[j][w] -= w_i[w]
    print(ret)

"""
後ろのほうからやってく？

ある時の操作がだいぶ後の操作に影響を与える可能性がある
共通部分を考えていくイメージ
ある範囲間の共通部分は何か？
dp[あるエクササイズ][あるエクササイズ][種類]


全探索作戦で行く

"""
