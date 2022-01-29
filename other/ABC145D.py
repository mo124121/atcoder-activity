from math import factorial

X, Y = map(int, input().split())
MOD = 10 ** 9 + 7


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


if (X + Y) % 3 == 0 and X // 2 <= Y and Y / 2 <= X:
    jump = (X + Y) // 3
    choice = jump * 2 - X
    binominal = Binominal((X + Y) // 3, MOD)
    ret = binominal.calc(jump, choice)
    print(ret)
else:
    print(0)
