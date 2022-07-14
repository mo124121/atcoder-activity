N = int(input())
X = input()
one_count = X.count("1")


mod_m = one_count - 1
mod_p = one_count + 1
memo_m = []
memo_p = []
for i in range(N):
    v0 = pow(2, i, mod_m) if mod_m > 0 else 0
    v1 = pow(2, i, mod_p)
    memo_m.append(v0)
    memo_p.append(v1)
memo_m.reverse()
memo_p.reverse()


sum_m = 0
sum_p = 0
for m, p, x in zip(memo_m, memo_p, X):
    if x == "1":
        sum_m += m
        sum_p += p


def popcount(x):
    return bin(x).count("1")


for i, x in enumerate(X):
    if x == "1":
        if mod_m == 0:
            print(0)
            continue
        s = (sum_m - memo_m[i]) % mod_m
    else:
        s = (sum_p + memo_p[i]) % mod_p

    ret = 1
    while s != 0:
        s = s % popcount(s)
        ret += 1
    print(ret)


"""
初期の割るbit数はpopcount(X)-1 or popcount(X)+1
各bitに対して上記MODを事前計算し、合計しておく
あとはたぶん大した回数は必要ないはず、たぶん

AC後解説
f(n)は事前計算可能なので先にしておくとよい
"""
