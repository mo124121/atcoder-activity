D, G = map(int, input().split())
C = [0] * D
P = [0] * D
max_s = 0
for i in range(D):
    P[i], C[i] = map(int, input().split())
    max_s += P[i] * (i + 1) + C[i]
INF = 10**10

G //= 100
dp = [[INF] * (max_s + 1) for _ in range(D + 1)]  # 解いた問題の個数

dp[0][0] = 0

for i in range(D):
    p = P[i]
    c = C[i] // 100
    for p_s in range(max_s - p * (i + 1) - c + 1):
        if dp[i][p_s] == INF:
            continue
        for j in range(p):
            dp[i + 1][p_s + (i + 1) * j] = min(
                dp[i + 1][p_s + (i + 1) * j], dp[i][p_s] + j
            )
        dp[i + 1][p_s + (i + 1) * p + c] = min(
            dp[i + 1][p_s + (i + 1) * p + c], dp[i][p_s] + p
        )
ret = INF
for p_s in range(G, max_s + 1):
    ret = min(ret, dp[D][p_s])
print(ret)
