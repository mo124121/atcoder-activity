H, N = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

INF = 10**18
dp = [INF] * (H + 1)
dp[0] = 0
for i in range(N):
    nxt = [INF] * (H + 1)
    a, b = AB[i]
    for h in range(H + 1):
        nxt[h] = min(nxt[h], dp[h])
        nxt[min(H, h + a)] = min(nxt[min(H, h + a)], nxt[h] + b)
    dp = nxt
print(dp[H])
