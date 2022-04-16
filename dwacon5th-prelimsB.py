from heapq import heappop, heappush


N, K = map(int, input().split())
a = list(map(int, input().split()))

beauty = [[0] * N for _ in range(N)]
h = []
for i in range(N):
    beauty[i][i] = a[i]
    heappush(h, -a[i])

for l in range(N):
    for r in range(l + 1, N):
        beauty[l][r] = beauty[l][r - 1] + a[r]
        heappush(h, -beauty[l][r])

l = []
ret = 0
for i in reversed(range(31)):
    ret_i = ret + (1 << i)
    while len(h):
        v = -heappop(h)
        if v < 1 << i:
            heappush(h, -v)
            break
        l.append(v)
    r = []
    for li in l:
        if (li & ret_i) == ret_i:
            r.append(li)

    if len(r) >= K:
        l = r
        ret = ret_i


print(ret)
"""
N<10**3

あーK個かあ

とりあえず[l,r]の全パターンの美しさを求める

bitの重なりが一番残るやつを選ぶ感じ
上のビットからK個以上たってる集合を順次選んでいくイメージ

"""
