L = input()

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


bn = Binominal(len(L) + 1)


ret = 1
for i, c in enumerate(L[::-1]):
    if c == "1":
        ret += pow(3, i, MOD)
        ret %= MOD
print(ret)
"""
L<2**100001
でっかい

露骨にbit演算する感じ

a+b=a^b

XORはどちらかのビットが立っていたら1　それ以外は0
とすると、どちらかのbitが立っている場合を全部数える？

繰り上がりについて考える
10
01
11

001
011
010
100

一致しなさそう…？

そんなに簡単な話か？

いったんどちらかbitが立ってるものを数え上げてみる
上の桁がある状態で一致させられるか？
できないんじゃね？
いやできるわ、落ち着け

1回シミュレーションする


立ってるbit数分のパターンができる
とすると、
ビット数nとすると
ΣnCi*2**i
i

解説後
桁DP...

"""
from collections import defaultdict

T = 8  # 111
count = defaultdict(list)
for i in range(0, T + 1):
    for j in range(T - i + 1):
        if i + j == i ^ j:
            count[i + j].append((bin(i + j), bin(i), bin(j)))
for k, l in count.items():
    print(bin(k))
    for r in l:
        print(*r)

"""
0b0
0b0 0b0 0b0
0b1
0b1 0b0 0b1
0b1 0b1 0b0
0b10
0b10 0b0 0b10
0b10 0b10 0b0
0b11
0b11 0b0 0b11
0b11 0b1 0b10
0b11 0b10 0b1
0b11 0b11 0b0
0b100
0b100 0b0 0b100
0b100 0b100 0b0
0b101
0b101 0b0 0b101
0b101 0b1 0b100
0b101 0b100 0b1
0b101 0b101 0b0
0b110
0b110 0b0 0b110
0b110 0b10 0b100
0b110 0b100 0b10
0b110 0b110 0b0
0b111
0b111 0b0 0b111
0b111 0b1 0b110
0b111 0b10 0b101
0b111 0b11 0b100
0b111 0b100 0b11
0b111 0b101 0b10
0b111 0b110 0b1
0b111 0b111 0b0
0b1000
0b1000 0b0 0b1000
0b1000 0b1000 0b0
"""
