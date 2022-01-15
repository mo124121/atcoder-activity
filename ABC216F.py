N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

AB = [(A[i], B[i]) for i in range(N)]
AB.sort()

A = [AB[i][0] for i in range(N)]
B = [AB[i][1] for i in range(N)]


ret = 0

dp = [[0] * (A[N - 1] + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(A[N - 1] + 1):
        dp[i + 1][j] = dp[i][j]
        if B[i] <= j:
            dp[i + 1][j] += dp[i][j - B[i]]
            dp[i + 1][j] %= MOD
        if j <= A[i] - B[i]:
            ret += dp[i][j]
            ret %= MOD

print(ret)
