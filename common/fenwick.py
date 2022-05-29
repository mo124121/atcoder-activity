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
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        return self.sum(i) - self.sum(i - 1)

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
        return self.ft0.sum(i) + self.ft1.sum(i) * i

    def get(self, i):
        return self.sum(i + 1) - self.sum(i)

    def show(self):
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


if __name__ == "__main__":
    ft = FenwickTree(10)
    ft.add(6, 5)
    ft.show()

    rft = RangedFenwick(10)
    rft.add_range(9, 10, 5)
    rft.show()
