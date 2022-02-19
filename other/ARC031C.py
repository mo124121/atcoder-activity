N = int(input())
B = list(map(int, input().split()))


class FenwickTree:
    def __init__(self, n, init_data=0):
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


ft = FenwickTree(N, 1)

C = [(B[i], i + 1) for i in range(N)]
C.sort()

ret = 0

for h, i in C:
    l_count = ft.sum(i)
    r_count = ft.sum(N) - l_count
    ret += min(l_count - 1, r_count)
    ft.add(i, -1)

print(ret)
