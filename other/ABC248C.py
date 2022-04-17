N, M, K = map(int, input().split())

dp = [[0] * (N * M + 1) for _ in range(N + 1)]
dp[0][0] = 1
MOD = 998244353

for i in range(N):
    for j in range(i * M + 1):
        dp[i][j] %= MOD
        for k in range(1, M + 1):
            dp[i + 1][j + k] += dp[i][j]

ret = 0
for j in range(K + 1):
    ret += dp[N][j]
    ret %= MOD
print(ret)

"""
考察

あせると良くない
M,N<50
K<2500

追加する毎に作れる数をカウントしていくイメージ
dpで解ける

"""
