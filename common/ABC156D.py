class Binominal:
    def __init__(self, N, MAX_K, MOD):
        fact_inv = [1, 1]
        inv = [0, 1]
        for i in range(2, MAX_K + 1):
            inv.append((MOD - inv[MOD % i] * (MOD // i)) % MOD)
            fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)
        com = [1]
        for i in range(1, MAX_K + 1):
            com.append((com[-1] * ((N - i + 1) * inv[i] % MOD)) % MOD)
        self.com = com

    def calc(self, k):
        return self.com[k]


n, a, b = map(int, input().split())
MOD = 10**9 + 7

bn = Binominal(n, max(a, b), MOD)

ret = (pow(2, n, MOD) - 1 - bn.calc(a) - bn.calc(b)) % MOD
print(ret)

"""
mod内の引き算ができれば余裕？
n<10**9
単純に数え上げはできないが、愚直は下記

ΣnCi  -nCa-nCb

a,b<2*10**5
この制約・・・？何かに使える？

逆に低くとも2*10**5以降のmod部分は変わらない

2項係数の和をうまく計算して、
nCaとnCbを計算すればいい

2項係数の和は2**n (i=0...n)

あとはnCaの計算

ある程度高速に行きたいが、さて
何も考えずにやっても間に合う？

nがでかいときの2項係数ライブラリを使ってAC

"""
