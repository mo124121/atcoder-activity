class Binominal:
    def __init__(self, N):
        c = [[0] * (N + 1) for _ in range(N + 1)]

        c[0][0] = 1
        for i in range(N):
            for j in range(i + 1):
                c[i + 1][j] += c[i][j] / 2
                c[i + 1][j + 1] += c[i][j] / 2
        self.c = c

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.c[n][r]


N, D = map(int, input().split())
X, Y = map(int, input().split())

if X % D != 0 or Y % D != 0:
    print(0)
    exit()

X //= D
Y //= D

bn = Binominal(N)
ret = 0
for c_x in range(0, N + 1):
    c_y = N - c_x
    r = bn.calc(N, c_x)
    if X <= c_x and (c_x - X) % 2 == 0:
        r *= bn.calc(c_x, (c_x + X) // 2)
    else:
        r = 0
    if Y <= c_y and (c_y - Y) % 2 == 0:
        r *= bn.calc(c_y, (c_y + Y) // 2)
    else:
        r = 0
    ret += r
print(ret)
