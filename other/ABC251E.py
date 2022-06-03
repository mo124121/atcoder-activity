N = int(input())
A = list(map(int, input().split()))

ret = 0
INF = 10**15
dp = [[INF] * 2 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    dp[i + 1][0] = dp[i][1]
    dp[i + 1][1] = A[i] + min(dp[i][0], dp[i][1])
ret = dp[N][0]

dp = [[INF] * 2 for _ in range(N + 1)]
dp[0][1] = 0
for i in range(N):
    dp[i + 1][0] = dp[i][1]
    dp[i + 1][1] = A[i] + min(dp[i][0], dp[i][1])
ret = min(ret, dp[N][1])

print(ret)
