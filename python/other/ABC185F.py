class FenwickTree:
    def __init__(self, n, init_data=0):
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def xor(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret ^= self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] ^= x
            i += i & -i

    def get(self, i):
        return self.xor(i) ^ self.xor(i - 1)


N, Q = map(int, input().split())
A = list(map(int, input().split()))

ft = FenwickTree(N + 1)
for i, a in enumerate(A):
    ft.add(i + 1, a)

for q in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        ft.add(x, y)
    else:
        print(ft.xor(y) ^ ft.xor(x - 1))

"""
Fenwickを書き換えたらできそう
AC

"""
