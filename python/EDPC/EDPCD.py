N, W = map(int, input().split())
dp = [0] * (W + 1)

for i in range(N):
    nxt = [0] * (W + 1)
    w, v = map(int, input().split())
    for j in range(W):
        nxt[j] = max(nxt[j], dp[j])
        if j + w <= W:
            nxt[j + w] = max(nxt[j + w], dp[j] + v)
    dp = nxt
print(max(dp))
