N, K = map(int, input().split())
a = list(map(int, input().split()))

beauty = [[0] * N for _ in range(N)]
vs = []
for i in range(N):
    beauty[i][i] = a[i]
    vs.append(a[i])

for l in range(N - 1):
    for r in range(l + 1, N):
        beauty[l][r] = beauty[l][r - 1] + a[r]
        vs.append(beauty[l][r])


ret = 0
for i in reversed(range(40)):
    ret_i = ret + (1 << i)

    r = []
    for v in vs:
        if (v & ret_i) == ret_i:
            r.append(v)

    if len(r) >= K:
        ret = ret_i


print(ret)
"""
N<10**3

あーK個かあ

とりあえず[l,r]の全パターンの美しさを求める

bitの重なりが一番残るやつを選ぶ感じ
上のビットからK個以上たってる集合を順次選んでいくイメージ

教訓
最大値がどのあたりに来るかちゃんと考察すべき
"""
