N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
dp = [[0] * (3002) for _ in range(N)]
for j in range(A[0], B[0] + 1):
    dp[0][j] = 1

for i in range(1, N):
    if i > 1:
        for j in range(3002):
            dp[i - 1][j] += dp[i - 1][j - 1]

    for j in range(A[i - 1], B[i - 1] + 1):
        # for k in range(max(A[i], j), B[i] + 1):
        if j <= B[i - 1]:
            dp[i][max(A[i], j)] = (dp[i][max(A[i], j)] + dp[i - 1][j]) % MOD
            dp[i][B[i] + 1] = (dp[i][B[i] + 1] - dp[i - 1][j]) % MOD
for j in range(3002):
    dp[N - 1][j] += dp[N - 1][j - 1]
    dp[N - 1][j] %= MOD


ret = 0
for d in dp[N - 1][:3001]:
    ret = (ret + d) % MOD
print(ret)
"""
3000という数字はDPのサインなのかもしれない・・・？

dp[i][j]=i番目までの数列で、最大値jまで使ったパターン数

TLE,どうする？

なんかいもすくさい

"""
