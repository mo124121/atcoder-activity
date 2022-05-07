N, M = map(int, input().split())
from collections import defaultdict, deque

INF = 10**10
memo = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    memo[a][b] = c
for i in range(1, N + 1):
    memo[i][i] = 0


ret = 0

for k in range(1, N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])
            if memo[i][j] != INF:
                ret += memo[i][j]

print(ret)


"""
ワーシャルフロイド
N<400
N**3<2*10*7

あーKまでの距離しかできない、これはDAGを利用して探索
全てのノードを起点に深い方向まで伸ばしていく

たまには再帰で書くか
メモ化したら速くはなりそうだが面倒なのでしない

楽勝モードだったけど、経由できる都市数に制限数はある最小経路…
ダイクストラを改造する必要がありそう

足踏みもできるってこと？

数字が合わない
あーこれややこしい、最短経路といいつつ最短じゃない
書き換えたら間に合わなくなりそう

解説後
やっぱりワーシャルフロイドやんけ

ふぁーーーー問題よみまちがえてるーーーー

"""
