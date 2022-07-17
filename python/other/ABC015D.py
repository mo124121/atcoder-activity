from collections import defaultdict


W = int(input())
N, K = map(int, input().split())

dp = [[[0] * (W + 1) for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N):
    A, B = map(int, input().split())

    for k in range(K + 1):
        for w in range(W + 1):
            dp[i + 1][k][w] = max(dp[i + 1][k][w], dp[i][k][w])
            if w + A <= W and k < K:
                dp[i + 1][k + 1][w + A] = max(dp[i + 1][k + 1][w + A], dp[i][k][w] + B)

ret = 0
for k in range(K + 1):
    for w in range(W + 1):
        ret = max(ret, dp[N][k][w])


print(ret)

"""
間に合わない
"""
