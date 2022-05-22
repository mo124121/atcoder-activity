from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


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


@lru_cache(maxsize=None)
def factorial(x, MOD):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1, MOD) % MOD


N, A, B, C, D = map(int, input().split())
MOD = 10**9 + 7

ret = 0

dp = [[ModInt(0, MOD)] * (N + 1) for _ in range(B + 1)]
dp[A - 1][N] = ModInt(1, MOD)
for i in range(A, B + 1):
    for j in range(N + 1):
        if dp[i - 1][j] == 0:
            continue
        tmp_j = factorial(j, MOD)
        # 一つもグループを作らない時
        dp[i][j] += dp[i - 1][j]
        # k個グループを作る時
        for k in range(C, D + 1):
            if j - k * i < 0:
                break
            tmp = ModInt(1, MOD) * tmp_j
            tmp /= factorial(j - k * i, MOD)
            tmp /= pow(factorial(i, MOD), k, MOD)
            tmp /= factorial(k, MOD)
            dp[i][j - k * i] += dp[i - 1][j] * tmp
print(dp[B][0])

"""
dp[i][j]:i番目まで使って、残りj個残っている場合のパターン数

"""
