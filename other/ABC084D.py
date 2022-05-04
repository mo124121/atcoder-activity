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


Q = int(input())

L = [0] * Q
R = [0] * Q
for i in range(Q):
    L[i], R[i] = map(int, input().split())


N = 10**5 + 100

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
i = 2
while i**2 <= N:
    if is_prime[i]:
        j = i * 2
        while j <= N:
            is_prime[j] = False
            j += i
    i += 1

bit = FenwickTree(N + 1)
for i in range(N + 1):
    if is_prime[i]:
        if i % 2 == 1:
            if is_prime[(i + 1) // 2]:
                bit.add(i, 1)


ret = []
for q in range(Q):
    ret.append(bit.sum(R[q] + 1) - bit.sum(L[q] - 1))
print(*ret, sep="\n")
"""
素数探す->BITで個数カウント

解説後
bitでなくとも累積和でいいな
"""
