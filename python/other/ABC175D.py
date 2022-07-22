N, K = map(int, input().split())
P = list(map(int, input().split()))
P = [p - 1 for p in P]
C = list(map(int, input().split()))

BIT = 30
dbl = [[0] * (N) for _ in range(BIT + 1)]
warp = [[0] * (N) for _ in range(BIT + 1)]
warp[0] = list(range(N))
warp[1] = P

for i in range(N):
    dbl[1][i] = C[P[i]]

for bit in range(1, BIT):
    for i in range(N):
        warp[bit + 1][i] = warp[bit][warp[bit][i]]
        dbl[bit + 1][i] = dbl[bit][i] + dbl[bit][warp[bit][i]]


INF = 10**18
ret = max(C)
for i in range(N):
    prev = i
    k = K
    r = 0
    flag = False
    for bit in range(1, BIT + 1):
        if k >> (bit - 1) & 1:
            if dbl[bit][prev] > 0:
                r += dbl[bit][prev]
                prev = warp[bit][prev]
                flag = True
            else:
                k = (1 << bit) - 1
    if flag:
        ret = max(ret, r)


print(ret)

"""
間違っている
そもそもDではダブリングでないのでは？
"""
