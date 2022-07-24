N, K = map(int, input().split())
H = list(map(int, input().split()))
INF = 10**18
dp = [INF] * N
dp[0] = 0
for i in range(N - 1):
    for j in range(i + 1, min(i + K + 1, N)):
        dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

print(dp[N - 1])
