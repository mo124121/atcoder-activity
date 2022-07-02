N, W = map(int, input().split())
dp = [[[0] * (3 * N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
WV = []
for _ in range(N):
    WV.append(list(map(int, input().split())))

w0 = WV[0][0]
for i, (w, v) in enumerate(WV):
    w -= w0
    for j in range(N + 1):
        for k in range(3 * N + 1):
            dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
            if k + w <= 3 * N and j + 1 <= N:
                dp[i + 1][j + 1][k + w] = max(dp[i + 1][j + 1][k + w], dp[i][j][k] + v)

ret = 0
for j in range(N + 1):
    for k in range(3 * N + 1):
        if w0 * j + k <= W:
            ret = max(ret, dp[N][j][k])
print(ret)
