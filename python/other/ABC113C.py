from collections import defaultdict


N, M = map(int, input().split())
ret = []
count = defaultdict(int)
P = [0] * M
Y = [0] * M
for i in range(M):
    P[i], Y[i] = map(int, input().split())
YP = [(Y[i], P[i], i) for i in range(M)]
YP.sort()

for i in range(M):
    y, p, j = YP[i]
    count[p] += 1
    ret.append((j, count[p], p))
ret.sort()

for r in ret:
    print("{:06d}{:06d}".format(r[2], r[1]))
