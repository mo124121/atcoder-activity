N = int(input())
A = list(map(int, input().split()))
INF = 10**18
dp = [INF] * (N + 1)

dp[2] = A[0]

for i in range(2, N):
    dp[i + 1] = min(dp[i] + A[i - 1], dp[i + 1])
    if i + 2 <= N:
        dp[i + 2] = min(dp[i] + A[i], dp[i + 2])

ret = dp[-1]

dp = [INF] * (N)

dp[1] = A[-1]
for i in range(1, N - 1):
    dp[i + 1] = min(dp[i] + A[i - 1], dp[i + 1])
    if i + 2 <= N - 1:
        dp[i + 2] = min(dp[i] + A[i], dp[i + 2])

ret = min(ret, dp[-1])

print(ret)
