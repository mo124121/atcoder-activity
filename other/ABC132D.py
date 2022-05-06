N, K = map(int, input().split())
MOD = 10**9 + 7


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


bn = Binominal(N, MOD)

for i in range(1, K + 1):
    print(bn.calc(N - K + 1, i) * bn.calc(K - 1, i - 1) % MOD)

"""
選び方たくさん

N-K+1
の場所にどう配置するか？
1.まず一塊にするとして、どの位置に配置するか？
(N-K+1)Ci

2.次にその塊のそれぞれに何個入れていくか？
i**(K-i)

んー普通にできない？

8/14 WA
何か考慮が足りてなさそう

隙間がそもそも十分あるか？

2.が違ってそう
残った個数 K-i
o|ooo|oo
(K-i+(i-1))C(i-1)
=(K-i)C(i-1)

AC
サイズ的にパスカルの3角形でもいい
"""
