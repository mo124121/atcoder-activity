from collections import Counter


N = int(input())
T = [int(input()) for _ in range(N)]
T.sort()
T2 = Counter(T)
ret = 0
MOD = 10**9 + 7
e = 0
pat = 1
for t, count in T2.items():
    p = 1
    for c in range(count):
        e += t
        ret += e
        pat = pat * p % MOD
        p += 1
print(ret)
print(pat)


"""
待ち行列理論
小さいほうから累積和

パターン数だと？
ほなcounter使って数え上げましょ

"""
