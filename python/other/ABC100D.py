from itertools import product


N, M = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(N)]


ret = -(10**18)
for pat in product((1, -1), repeat=3):
    dp = [-(10**18)] * (M + 1)
    dp[0] = 0
    for i, (x, y, z) in enumerate(XYZ):
        score_i = x * pat[0] + y * pat[1] + z * pat[2]
        for j in reversed(range(min(M, i + 1))):
            dp[j + 1] = max(dp[j + 1], dp[j] + score_i)
    ret = max(ret, dp[M])
print(ret)
"""
各正負をbit全探索しつついいのを探る？
"""
