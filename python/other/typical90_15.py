N = int(input())


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


MOD = 10**9 + 7
bn = Binominal(N, MOD)

for k in range(1, N + 1):
    ret = 0
    a = 1
    while N - (k - 1) * (a - 1) >= a:
        ret += bn.calc(N - (k - 1) * (a - 1), a)
        ret %= MOD
        a += 1
    print(ret)
