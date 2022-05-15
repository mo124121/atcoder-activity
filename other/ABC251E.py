INF = 10**18

N = int(input())
A = [INF] + list(map(int, input().split()))

dp = [[INF] * 2 for _ in range(N + 1)]
dp[1][0] = 0
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]
ret = dp[N][1]

dp = [[INF] * 2 for _ in range(N + 1)]
dp[1][1] = A[1]
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + A[i]
ret = min(ret, *dp[N])
print(ret)
"""
dp[i][j]:i個目目までの行動で、j=0行動しない、j=1行動する場合の最小コスト

"""
