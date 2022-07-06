A, B, K = map(int, input().split())


class Binominal:
    def __init__(self, N):
        c = [[0] * (N + 1) for _ in range(N + 1)]

        c[0][0] = 1
        for i in range(N):
            for j in range(i + 1):
                c[i + 1][j] += c[i][j]
                c[i + 1][j + 1] += c[i][j]
        self.c = c

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        return self.c[n][r]


bn = Binominal(A + B)
ret = ""
while A + B > 0:
    c = bn.calc(A + B - 1, A - 1)
    if c >= K:
        A -= 1
        ret += "a"
    else:
        B -= 1
        ret += "b"
        K -= c


print(ret)
