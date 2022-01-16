H, W = map(int, input().split())
INF = H + W
s = [list(input()) for _ in range(H)]

dp = [[(INF, "#")] * (W + 1) for _ in range(H + 1)]

dp[1][0] = (0, ".")
dp[0][1] = (0, ".")

for i in range(H):
    for j in range(W):
        up_cost, up_stat = dp[i][j + 1]
        left_cost, left_stat = dp[i + 1][j]
        up_cost += int(up_stat == "." and s[i][j] == "#")
        left_cost += int(left_stat == "." and s[i][j] == "#")
        dp[i + 1][j + 1] = (min(up_cost, left_cost), s[i][j])

print(dp[H][W][0])
