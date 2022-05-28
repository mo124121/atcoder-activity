N, M, K = map(int, input().split())
MOD = 998244353
dp = [1] * (M)

if K == 0:
    print(pow(M, N, MOD))
    exit()

for i in range(N - 1):
    line_l = [0] * M
    line_r = [0] * M
    for j in range(M):
        if 0 <= j - K:
            line_l[j - K] += dp[j]
            line_l[j - K] %= MOD
        if j + K < M:
            line_r[j + K] += dp[j]
            line_l[j + K] %= MOD
    for i in range(M - 1):
        line_r[i + 1] += line_r[i]
        line_r[i + 1] %= MOD
    for i in range(M - 1, 0, -1):
        line_l[i - 1] += line_l[i]
        line_l[i - 1] %= MOD
    for i in range(M):
        dp[i] = line_r[i] + line_l[i]


print(sum(dp) % MOD)
