from collections import defaultdict


N, M = map(int, input().split())
G = defaultdict(list)
INF = 10 * 3 * N**2
dp = [[INF] * (N + 1) for _ in range(N + 1)]


for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    dp[a][b] = c
    dp[b][a] = c

for i in range(1, N + 1):
    dp[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

ret = 0

for v in range(1, N + 1):
    for c, e in G[v]:
        if c != dp[v][e]:
            ret += 1

print(ret)
