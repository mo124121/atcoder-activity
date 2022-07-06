class Binominal:
    def __init__(self, N, mod) -> None:
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]

        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % mod)
            inv.append((-inv[mod % i] * (mod // i)) % mod)
            factinv.append((factinv[-1] * inv[-1]) % mod)

        self.fact = fact
        self.factinv = factinv
        self.inv = inv
        self.mod = mod
        self.N = N

    def binominal(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


N, A, B, C, D = map(int, input().split())
MOD = 10**9 + 7

bn = Binominal(N, MOD)

ret = 0

dp = [[0] * (N + 1) for _ in range(B + 1)]
dp[A - 1][N] = 1
for i in range(A, B + 1):
    for j in range(N + 1):
        if dp[i - 1][j] == 0:
            continue
        # 一つもグループを作らない時
        dp[i][j] += dp[i - 1][j]
        # k個グループを作る時
        jn = j - i
        tmp = 1
        for k in range(1, D + 1):
            if jn < 0:
                break
            tmp *= bn.fact[jn + i] * bn.factinv[jn] * bn.factinv[i]
            tmp %= MOD
            if k >= C:
                dp[i][jn] += dp[i - 1][j] * tmp * bn.factinv[k]
                dp[i][jn] %= MOD
            jn -= i
print(dp[B][0])

"""
dp[i][j]:i番目まで使って、残りj個残っている場合のパターン数

"""
