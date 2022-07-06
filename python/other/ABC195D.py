from heapq import heappop, heappush


N, M, Q = map(int, input().split())
W = [] * N
V = [] * N
WV = [] * N
for i in range(N):
    WV.append(tuple(map(int, input().split())))
WV.sort()
X = list(map(int, input().split()))
ret = []
for i in range(Q):
    L, R = map(int, input().split())
    boxs = X[: L - 1] + X[R:]
    boxs.sort()
    h = []
    used = -1
    score = 0
    for size in boxs:
        for i in range(used + 1, N):
            w, v = WV[i]
            if w > size:
                break
            used = i
            heappush(h, -v)
        if len(h) > 0:
            score += -heappop(h)
    ret.append(score)
print(*ret, sep="\n")
