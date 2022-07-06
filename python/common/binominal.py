# パスカル modなし　O(N**2)
class Binominal:
    def __init__(self, N):
        c = [[0] * (N + 1) for _ in range(N + 1)]

        c[0][0] = 1
        for i in range(N):
            for j in range(i + 1):
                c[i + 1][j] += c[i][j]
                c[i + 1][j + 1] += c[i][j]
        self.c = c

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.c[n][r]


# 高速なの　O(N)
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


# nがでかいもの
class Binominal:
    def __init__(self, N, MAX_K, MOD):
        fact_inv = [1, 1]
        inv = [0, 1]
        for i in range(2, MAX_K + 1):
            inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
            fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)
        com = [1]
        for i in range(1, MAX_K + 1):
            com.append((com[-1] * ((N - i + 1) * inv[i] % MOD)) % MOD)
        self.com = com

    def calc(self, k):
        return self.com[k]


# 直接
def comb(n, r, MOD):
    r = min(r, n - r)
    if n == 0:
        return 1
    big = 1
    small = 1
    for i in range(1, r + 1):
        big *= n + 1 - i
        small *= i
    return big // small % MOD
