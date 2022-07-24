N, W = map(int, input().split())
INF = 10**18
dp = [INF] * (N * 1000 + 1)  # 価値
dp[0] = 0

for i in range(N):
    nxt = [INF] * (N * 1000 + 1)
    w, v = map(int, input().split())
    for vi in range(N * 1000):
        nxt[vi] = min(nxt[vi], dp[vi])
        if vi + v <= N * 1000 and dp[vi] + w <= W:
            nxt[vi + v] = min(nxt[vi + v], dp[vi] + w)
    dp = nxt

ret = 0
for vi in range(N * 1000 + 1):
    if dp[vi] <= W:
        ret = max(ret, vi)

print(ret)
