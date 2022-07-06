N, Q, X = map(int, input().split())
W = list(map(int, input().split()))
B1 = 30
INF = 10**18
dub = [[INF] * (N) for _ in range(B1 + 1)]

for i in range(N):
    dub[0][i] = W[i]

for i in range(B1):
    for j in range(N):
        if dub[i][j] < INF and dub[i][(j + 2**i) % N] < INF:
            dub[i + 1][j] = dub[i][j] + dub[i][(j + 2**i) % N]

shift = [0] * N
size = [0] * N

for i in range(N):
    total = 0
    t = i
    for j in reversed(range(B1)):
        if total + dub[j][t] < X:
            total += dub[j][t]
            t = (t + 2**j) % N
            size[i] += 2**j
    shift[i] = (t + 1) % N
    size[i] += 1

B2 = 40
dub_k = [[0] * (N) for _ in range(B2 + 1)]
for i in range(N):
    dub_k[0][i] = shift[i]
for i in range(B2):
    for j in range(N):
        dub_k[i + 1][j] = dub_k[i][dub_k[i][j]]

ret = []
for _ in range(Q):
    k = int(input())
    k -= 1
    r = 0
    for j in range(B2):
        if k >> j & 1 == 1:
            r = dub_k[j][r]
    ret.append(size[r])

for r in ret:
    print(r)
