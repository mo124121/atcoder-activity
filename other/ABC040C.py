N = int(input())
A = list(map(int, input().split()))
INF = 10**10
dp = [INF] * N
dp[0] = 0
dp[1] = abs(A[1] - A[0])
for i in range(2, N):
    dp[i] = min(dp[i], dp[i - 1] + abs(A[i] - A[i - 1]))
    dp[i] = min(dp[i], dp[i - 2] + abs(A[i] - A[i - 2]))

print(dp[N - 1])

"""
たぶんけんちょん本でみたやつや
典型DP
dpで各2パターンの遷移をさせつつ、最小コストだけ保管する
"""
