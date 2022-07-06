class FenwickTree:
    def __init__(self, n, init_data=0, MOD=100):
        self.size = n
        self.tree = [0] * (n + 1)
        self.MOD = MOD
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            ret %= MOD
            i -= i & -i
        return ret

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= MOD
            i += i & -i

    def get(self, i):
        return (self.sum(i) - self.sum(i - 1)) % MOD

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
MOD = 998244353

ft_A = FenwickTree(N, MOD=MOD)
ft_Ai = FenwickTree(N, MOD=MOD)
ft_Ai2 = FenwickTree(N, MOD=MOD)
for i, a in enumerate(A):
    ft_A.add(i, a % MOD)
    ft_Ai.add(i, a * i % MOD)
    ft_Ai2.add(i, a * i * i % MOD)


ret = []
inv2 = pow(2, MOD - 2, MOD)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x, v = q
        x -= 1
        ft_A.add(x, (v - A[x]) % MOD)
        ft_Ai.add(x, (v - A[x]) * x % MOD)
        ft_Ai2.add(x, (v - A[x]) * x * x % MOD)
        A[x] = v
    else:
        _, x = q
        x -= 1
        S_A = ft_A.sum(x)
        S_Ai = ft_Ai.sum(x)
        S_Ai2 = ft_Ai2.sum(x)
        r = (S_Ai2 - S_Ai * (2 * x + 3) + S_A * (x + 1) * (x + 2)) * inv2 % MOD
        ret.append(r)

print(*ret, sep="\n")
