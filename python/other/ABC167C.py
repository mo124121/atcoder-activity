from itertools import product


N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
INF = 10**10
cmin = INF
for pat in product((False, True), repeat=N):
    total = [0] * (M + 1)

    for i, p in enumerate(pat):
        if p:
            for j in range(M + 1):
                total[j] += CA[i][j]

    flag = True
    for t in total[1:]:
        if t < X:
            flag = False
            break
    if flag and cmin > total[0]:
        cmin = total[0]


if cmin == INF:
    print(-1)
else:
    print(cmin)
