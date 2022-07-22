N = int(input())

ret = [[0] * N for _ in range(N)]

v = 1
for i in range(N):
    for j in range(0, N, 2):
        ret[i][j] = v
        v += 1
    for j in range(1, N, 2):
        ret[i][j] = v
        v += 1

for r in ret:
    print(*r)
