N = int(input())
MOD = 998244353
dp = [[0] * 10 for _ in range(N)]
for j in range(1, 10):
    dp[0][j] = 1

for i in range(N - 1):
    for j in range(1, 10):
        if j != 9:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD

        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
        if j != 1:
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

ret = 0
for j in range(1, 10):
    ret += dp[N - 1][j]
    ret %= MOD

print(ret)
