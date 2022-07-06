# https://qiita.com/wotsushi/items/c936838df992b706084c
# ちょい改変


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
