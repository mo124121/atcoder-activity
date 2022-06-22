N = int(input())

ret = [[0] * N for _ in range(N)]

for h in range(N):
    for w1 in range((N + 1) // 2):
        ret[h][w1 * 2] = h * N + 1 + w1
    for w2 in range(N // 2):
        ret[h][w2 * 2 + 1] = h * N + 2 + w2 + w1

for r in ret:
    print(*r)
