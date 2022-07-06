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


n, a, b = map(int, input().split())
MOD = 10**9 + 7


def nCr(n, r):
    md = ModInt(1, MOD)
    for i in range(n, n - r, -1):
        md *= i
    for i in range(1, r + 1):
        md /= i
    return md


ret = ModInt(2, MOD) ** n - 1 - nCr(n, a) - nCr(n, b)
print(ret)

"""
mod内の引き算ができれば余裕？
n<10**9
単純に数え上げはできないが、愚直は下記

ΣnCi  -nCa-nCb

a,b<2*10**5
この制約・・・？何かに使える？

逆に低くとも2*10**5以降のmod部分は変わらない

2項係数の和をうまく計算して、
nCaとnCbを計算すればいい

2項係数の和は2**n (i=0...n)

あとはnCaの計算

ある程度高速に行きたいが、さて
何も考えずにやっても間に合う？

nがでかいときの2項係数ライブラリを使ってAC

解説後 mod intを使うべし invがとれる

"""
