N, M, K = map(int, input().split())
MOD = 998244353


class Binominal:
    def __init__(self, N, mod) -> None:
        fact = [1, 1]
        factinv = [1, 1]
        inv = [0, 1]

        for i in range(2, N + 1):
            fact.append((fact[-1] * i) % mod)
            inv.append((-inv[mod % i] * (mod // i)) % mod)
            factinv.append((factinv[-1] * inv[-1]) % mod)

        self.fact = fact
        self.factinv = factinv
        self.inv = inv
        self.mod = mod
        self.N = N

    def calc(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod


bino = Binominal(N, MOD)

ret = 0
for k in range(K + 1):
    ret += bino.calc(N - 1, k) * M * (pow((M - 1), (N - 1 - k), MOD))
    ret %= MOD
print(ret)

"""
見るからにdp
dp[i][j]: i個までのブロックでj組のペアがあるパターン

N*K 10^5**2だから間に合わない…
長さ半分にして半分全列挙
それでも間に合わない気がする、制約条件的にない

普通にdpしたらええんちゃうん？

となりあう分、Nが減って個数カウントしていくイメージ

k=0の時
M*(M-1)^(N-1)*combi(N,0)
k=1の時
M*(M-1)^(N-2)
...
k=K
M*(M-1)^(N-K-1) * combi(N-1,K)

"""
