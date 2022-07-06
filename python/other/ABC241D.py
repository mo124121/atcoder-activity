# https://atcoder.jp/contests/abc241/submissions/29718960
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


def coordinate_compression(X):
    return {x: i for i, x in enumerate(sorted(list(set(X))))}


N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]
D = coordinate_compression([Q[i][1] for i in range(N)])
D_r = [0] * (len(D))
for k, v in D.items():
    D_r[v] = k

ft = FenwickTree(len(D))

ret = []
for i in range(N):
    if Q[i][0] == 1:
        x = Q[i][1]
        ft.add(D[x], 1)
    else:
        x, k = Q[i][1:]
        if Q[i][0] == 2:
            sum_x = ft.sum(D[x])
            if sum_x < k:
                ret.append(-1)
            else:
                ret.append(D_r[ft.lower_bound(sum_x - k + 1)])
        else:
            sum_x = ft.sum(D[x] - 1)
            if ft.sum(len(D) - 1) - sum_x < k:
                ret.append(-1)
            else:
                ret.append(D_r[ft.lower_bound(sum_x + k)])
print(*ret, sep="\n")
