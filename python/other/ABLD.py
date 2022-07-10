class SegmentTree:
    def __init__(self, N, init_value=-1, INF=-(10**15)) -> None:
        n = 1
        while n < N:
            n <<= 1

        self.n = n
        self.INF = INF
        self.elements = [init_value] * (2 * n - 1)

    def update(self, i, x):
        i += self.n - 1
        self.elements[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.elements[i] = max(self.elements[i * 2 + 1], self.elements[i * 2 + 2])

    def update_range(self, l, r, x):
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.n - 1
        r += self.n - 1
        self.elements[l:r] = x
        while 0 < l < r:
            l = (l - 1) // 2
            r = r // 2
            for i in range(l, r):
                self.elements[i] = max(
                    self.elements[i * 2 + 1], self.elements[i * 2 + 2]
                )

    def query(self, l, r):
        l += self.n - 1
        r += self.n - 1
        res = self.INF
        while l < r:
            res = max(max(res, self.elements[l]), self.elements[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res


N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
MAX_RANGE = 4 * 10**5
segtree = SegmentTree(MAX_RANGE, init_value=0)

for a in A:
    m = segtree.query(max(0, a - K), min(MAX_RANGE, a + K + 1))
    segtree.update(a, m + 1)

print(segtree.query(0, MAX_RANGE))
