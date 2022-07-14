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


N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7
bn = Binominal(N + 1, MOD)

A.sort()

maxsum = 0
for i in range(K - 1, N):
    maxsum += A[i] * bn.binominal(i, K - 1)
    maxsum %= MOD
A.reverse()
minsum = 0
for i in range(K - 1, N):
    minsum += A[i] * bn.binominal(i, K - 1)
    minsum %= MOD

print((maxsum - minsum) % MOD)
