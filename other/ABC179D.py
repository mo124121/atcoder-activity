N, K = map(int, input().split())
MOD = 998244353
LR = []
for _ in range(K):
    LR.append(list(map(int, input().split())))

LR.sort()
dp = [0] * (N + 2)
dp[1] = 1
dp[2] = -1

for i in range(1, N):
    for l, r in LR:
        l2 = min(N + 1, i + l)
        dp[l2] += dp[i]
        dp[l2] %= MOD
        r2 = min(N + 1, i + r + 1)
        dp[r2] -= dp[i]
        dp[r2] %= MOD
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD
print(dp[N])

"""
累積和DPっぽい

まずソート

累積和じゃなくても間に合う？
間に合わない発想が違う

K<10を見通していた
で、どうする？

bitでmodでもするか？

累積和でたたいていく

自力AC

解説
maspy氏の形式的べき級数を読むべし

fenwickでやったらどうなる？結局DPと同じ感じになるのでは？

"""
