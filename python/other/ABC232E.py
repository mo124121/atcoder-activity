H, W, K = map(int, input().split())
h1, w1, h2, w2 = map(int, input().split())

dp = [[0] * 4 for _ in range(K + 1)]
if (h1, w1) == (h2, w2):
    dp[0][0] = 1
elif w1 == w2:
    dp[0][1] = 1
elif h1 == h2:
    dp[0][2] = 1
else:
    dp[0][3] = 1

MOD = 998244353
for i in range(K):
    dp[i + 1][0] += dp[i][1] + dp[i][2]
    dp[i + 1][1] += dp[i][0] * (H - 1) + dp[i][1] * (H - 2) + dp[i][3]
    dp[i + 1][2] += dp[i][0] * (W - 1) + dp[i][2] * (W - 2) + dp[i][3]
    dp[i + 1][3] += dp[i][1] * (W - 1) + dp[i][2] * (H - 1) + dp[i][3] * (H - 2 + W - 2)
    for j in range(4):
        dp[i + 1][j] %= MOD

print(dp[K][0])
