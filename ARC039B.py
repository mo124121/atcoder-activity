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


N, K = map(int, input().split())

if K >= N:
    bn = Binominal(N, 10**9 + 7)
    ret = bn.calc(N, K % N)
else:
    bn = Binominal(N + K, 10**9 + 7)
    ret = bn.calc(N + K - 1, K)
print(ret)

"""
考察
偏りがないのが一番でかくなるはず
NC(KmodN)

0の全列挙がわからん
x0x0xx
(N+1)CK ???

"""
