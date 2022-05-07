N, M = map(int, input().split())
from collections import defaultdict, deque


G = defaultdict(list)
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
INF = 10**10
memo = [[[INF] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]


for i in range(1, N + 1):
    q = deque()
    t = 0
    k = 0
    seen = set()
    q.append((t, i, k))
    while len(q):
        t, node, k = q.popleft()
        memo[k][i][node] = min(t, memo[k][i][node])
        if k == N:
            continue
        for nxt, c in G[node]:
            q.append((t + c, nxt, k + 1))

ret = 0
for s in range(N + 1):
    for t in range(N + 1):
        c = INF
        for k in range(N + 1):
            cn = memo[k][s][t]
            c = min(c, cn)
            memo[k][s][t] = c
            if c != INF:
                ret += c


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



"""
