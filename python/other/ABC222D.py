N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
NUM_MAX = max(*A, *B)
MOD = 998244353
dp = [[0] * (NUM_MAX + 1) for _ in range(N + 1)]
dp[0][0] = 1
ways = [0] * (NUM_MAX + 1)
for i in range(N):
    ways[0] = dp[i][0]
    for j in range(1, NUM_MAX + 1):
        ways[j] = (ways[j - 1] + dp[i][j]) % MOD

    for j in range(A[i], B[i] + 1):
        dp[i + 1][j] = (dp[i + 1][j] + ways[j]) % MOD


ret = 0
for d in dp[N][: NUM_MAX + 1]:
    ret = (ret + d) % MOD
print(ret)
"""
3000という数字はDPのサインなのかもしれない・・・？

dp[i][j]=i番目までの数列で、最大値jまで使ったパターン数

TLE,どうする？

なんかいもすくさい

解説後
もらうDP->いもす
たぶんもらうDPだと遷移情報を都度計算して、後合算するイメージ
配るDPだとdpテーブルで累積和とるイメージなのではないかと


"""
