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


class ModInt:
    MOD = -1

    def __init__(self, x, MOD):
        self.MOD = MOD
        self.x = x % self.MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x, self.MOD)
            if isinstance(other, ModInt)
            else ModInt(self.x + other, self.MOD)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x, self.MOD)
            if isinstance(other, ModInt)
            else ModInt(self.x - other, self.MOD)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x, self.MOD)
            if isinstance(other, ModInt)
            else ModInt(self.x * other, self.MOD)
        )

    def __truediv__(self, other):
        return (
            ModInt(self.x * pow(other.x, self.MOD - 2, self.MOD), self.MOD)
            if isinstance(other, ModInt)
            else ModInt(self.x * pow(other, self.MOD - 2, self.MOD), self.MOD)
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, self.MOD), self.MOD)
            if isinstance(other, ModInt)
            else ModInt(pow(self.x, other, self.MOD), self.MOD)
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x, self.MOD)
            if isinstance(other, ModInt)
            else ModInt(other - self.x, self.MOD)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(other.x * pow(self.x, self.MOD - 2, self.MOD), self.MOD)
            if isinstance(other, ModInt)
            else ModInt(other * pow(self.x, self.MOD - 2, self.MOD), self.MOD)
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, self.MOD), self.MOD)
            if isinstance(other, ModInt)
            else ModInt(pow(other, self.x, self.MOD), self.MOD)
        )


d = int(input())
MOD = 998244353

bn = Binominal(d * 2, MOD)
print(bn.binominal(d * 2, d) / ModInt(2, MOD))

"""
非初見、知ってるから解けるやつ
"""
