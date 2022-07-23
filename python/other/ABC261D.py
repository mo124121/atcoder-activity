from collections import defaultdict


N, M = map(int, input().split())
X = list(map(int, input().split()))
C = defaultdict(int)
for i in range(M):
    c, y = map(int, input().split())
    C[c] = y


INF = 10**18
dp = [[-INF] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i] + C[j + 1])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
ret = 0
for j in range(N + 1):
    ret = max(ret, dp[N][j])

print(ret)
