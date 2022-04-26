from collections import defaultdict, deque


N, X, Y = map(int, input().split())
# 初期化
INF = N * 2
dist = [[INF] * (N) for _ in range(N)]
G = defaultdict(list)
for i in range(N - 1):
    G[i].append(i + 1)
    G[i + 1].append(i)
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)

ret = [0] * (N)


# 最短距離算出
for i in range(N - 1):
    q = deque()
    d = 0
    q.append((i, d))
    dist[i][i] = d
    while len(q):
        j, d = q.popleft()
        for nxt in G[j]:
            if dist[i][nxt] == INF:
                dist[i][nxt] = d + 1
                q.append((nxt, d + 1))

# 数え上げ
for i in range(N - 1):
    for j in range(i + 1, N):
        ret[dist[i][j]] += 1


print(*ret[1:], sep="\n")


"""
直線+どっかがつながっているグラフ

N<2*10**3　微妙に小さい
N**2log(N)とかは行けそうN**3はつらい

順次幅探索をしていけば良い
ワーシャルフロイド?
"""
