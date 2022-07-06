from bisect import bisect_left


N, K = map(int, input().split())
X = list(map(int, input().split()))
if 0 in X:
    del X[X.index(0)]
    K -= 1
    if len(X) == 0:
        print(0)
        exit()

s = bisect_left(X, 0)
ret = 10**9

for i in range(N - K + 1):
    l = X[i]
    r = X[i + K - 1]
    if l * r > 0:
        ret = min(ret, max(abs(l), abs(r)))
    else:
        l = abs(l)
        r = abs(r)
        ret = min(ret, 2 * l + r, l + 2 * r)

print(ret)

"""
全部つけなくていい

とりあえずソートしたうえで、
左i個とって右K-i個とる場合（反対も）の時間を算出、全列挙

あんまりきれいな実装が思いつかない

AC後
配列をあれこれ準備するより、各要素に着目して処理を変えると案外シンプルになる

"""
