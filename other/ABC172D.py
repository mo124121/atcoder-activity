N = int(input())

A = [1] * (N + 1)
A[0] = 1

for i in range(2, N + 1):
    j = i
    while j <= N:
        A[j] += 1
        j += i

ret = 0
for i in range(1, N + 1):
    ret += i * A[i]
print(ret)


"""
約数の個数をどう定義するか？

うーん難しい
約数列挙したいが、果たして間に合うか？
一回やってみっか
いや、明らかに間に合わない気がする

とりあえず素数出して、うーん

式変形にトライしてみる
K*f(K)
ある値のNまでの倍数を足して良い
複数あるなら複数！これがつらい！

解説見る
高速ゼータ変換とか出てくる、ほんまに緑か？

動画解説見る
アー普通にやればいい調和級数ひでぶ


"""
