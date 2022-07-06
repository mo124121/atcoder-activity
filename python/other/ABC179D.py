MOD = 998244353


class FenwickTree:
    def __init__(self, n, init_data=0):
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            ret %= MOD
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= MOD
            i += i & -i

    def get(self, i):
        return (self.sum(i) - self.sum(i - 1)) % MOD

    def lower_bound(self, w):
        if w <= 0:
            return 0
        x = 0
        r = 1
        while r < self.size:
            r = r << 1
        length = r
        S = 0
        while length > 0:
            if length + x < self.size and self.tree[x + length] < w:
                w -= self.tree[x + length]
                x += length
            length = length >> 1
        return x

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


class RangedFenwick:
    def __init__(self, n, init_data=0) -> None:
        self.ft0 = FenwickTree(n + 1, init_data=init_data)
        self.ft1 = FenwickTree(n + 1)
        self.size = n

    def add_range(self, l, r, x):
        l += 1
        r += 1
        self.ft0.add(l, -x * (l - 1))
        self.ft0.add(r + 1, x * r)
        self.ft1.add(l, x)
        self.ft1.add(r + 1, -x)

    def add(self, i, x):
        self.ft0.add(i, x)

    def sum(self, i):
        return (self.ft0.sum(i) + self.ft1.sum(i) * i) % MOD

    def get(self, i):
        return (self.sum(i + 1) - self.sum(i)) % MOD

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


N, K = map(int, input().split())

LR = []
for _ in range(K):
    LR.append(list(map(int, input().split())))

LR.sort()
ft = RangedFenwick(N + 2)
ft.add(1, 1)

for i in range(1, N):
    v = ft.get(i - 1)
    for l, r in LR:
        l = min(N + 2, i + l - 1)
        r = min(N + 2, i + r - 1)
        ft.add_range(l, r, v)
print(ft.get(N - 1))

"""
累積和DPっぽい

まずソート

累積和じゃなくても間に合う？
間に合わない発想が違う

K<10を見通していた
で、どうする？

bitでmodでもするか？

累積和でたたいていく

自力AC

解説
maspy氏の形式的べき級数を読むべし

fenwickでやったらどうなる？結局DPと同じ感じになるのでは？

"""
