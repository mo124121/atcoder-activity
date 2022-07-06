N, M, K = map(int, input().split())
MOD = 998244353

Ginv = []
for _ in range(M):
    a, b = map(int, input().split())
    Ginv.append((a, b))

dp = [0] * (N + 1)
dp[1] = 1

for i in range(K):
    total = sum(dp) % MOD
    dpn = [0] + [total] * (N)
    for a, b in Ginv:
        dpn[a] -= dp[b]
        dpn[b] -= dp[a]
    for j in range(1, N + 1):
        dpn[j] -= dp[j]
        dpn[j] %= MOD
    dp = dpn
print(dp[1] % MOD)


"""
解説読んだ
DPまではイメージしつつ、数式の変形ができてない
pypyで何もしないとかなりギリギリ
"""
