H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(H)]

cum_sum = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(H):
    for w in range(W):
        cum_sum[h + 1][w + 1] = cum_sum[h + 1][w] + C[h][w] * ((-1) ** ((h + w) % 2))
for h in range(H):
    for w in range(W):
        cum_sum[h + 1][w + 1] += cum_sum[h][w + 1]

ret = 0

for u in range(H + 1):
    for l in range(W + 1):
        for d in range(H + 1):
            for r in range(W + 1):
                if cum_sum[d][r] - cum_sum[d][l] - cum_sum[u][r] + cum_sum[u][l] == 0:
                    ret = max(ret, (d - u) * (r - l))
print(ret)
