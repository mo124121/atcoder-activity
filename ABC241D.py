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


def coordinate_compression(X):
    return {x: i + 1 for i, x in enumerate(sorted(list(set(X))))}


N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]
D = coordinate_compression([Q[i][1] for i in range(N)])
D_r = [0] * (len(D) + 1)
for k, v in D.items():
    D_r[v] = k

ft = FenwickTree(N)

ret = []
for i in range(N):
    if Q[i][0] == 1:
        x = Q[i][1]
        ft.add(D[x], 1)
    else:
        x, k = Q[i][1:]
        if Q[i][0] == 2:
            sum_x = ft.sum(D[x] + 1)
            if sum_x < k:
                ret.append(-1)
                continue
            l = 0
            r = D[x] + 1
            while r - l > 1:
                m = l + (r - l) // 2
                sum_m = ft.sum(m)
                if sum_x - sum_m >= k:
                    l = m
                else:
                    r = m
            ret.append(D_r[r])
        else:
            sum_x = ft.sum(D[x] - 1)
            if ft.sum(N) - sum_x < k:
                ret.append(-1)
                continue
            l = D[x] - 1
            r = len(D)
            while r - l > 1:
                m = l + (r - l) // 2
                sum_m = ft.sum(m)
                if sum_m - sum_x >= k:
                    r = m
                else:
                    l = m
            ret.append(D_r[r])
print(*ret, sep="\n")
