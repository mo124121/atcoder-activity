from bisect import bisect


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


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

fwt = FenwickTree(N + 1)
for i, a in enumerate(A):
    fwt.add(i, a)

ret = []
for i in range(Q):
    x = int(input())
    j = bisect(A, x)
    b = x * j - fwt.sum(j - 1)
    b2 = fwt.sum(N) - fwt.sum(j - 1) - x * (N - j)
    r = b + b2
    ret.append(r)
print(*ret, sep="\n")
