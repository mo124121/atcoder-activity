INF = 10**18

N = int(input())
A = [INF] + list(map(int, input().split()))

dp = [INF] * (N + 1)
dp[1] = dp[2] = A[1]

for i in range(3, N + 1):
    dp[i] = min(min(dp[i - 2], dp[i - 1]) + A[i - 1], dp[i - 1] + A[i])

ret = dp[-1]

dp = [INF] * (N)
dp[0] = dp[1] = A[-1]

for i in range(2, N):
    dp[i] = min(min(dp[i - 1], dp[i - 2]) + A[i - 1], dp[i - 1] + A[i])

ret = min(ret, dp[-1])

print(ret)
