N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353
rest = sum(A[1:])

if rest > A[0] - K:
    print(0)
    exit()


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

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


ret = 1
binom = Binominal(MOD, MOD)
ret *= binom.calc(A[0] - K - rest + K - 1, K - 1)
ret % MOD


for i in range(1, N):
    ret *= binom.calc(A[i] + K - 1, K - 1)
    ret %= MOD

print(ret)
