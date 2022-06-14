N, K = map(int, input().split())
XY = []
INF = 2 * 10**18
for i in range(N):
    XY.append(tuple(map(int, input().split())))

D = [[0] * N for _ in range(N)]

for i in range(N):
    xi, yi = XY[i]
    for j in range(N):
        xj, yj = XY[j]
        D[i][j] = (xi - xj) ** 2 + (yi - yj) ** 2

dp = [[INF] * (1 << N) for _ in range(K)]
for bit in range(1 << N):
    dist = 0
    for i in range(N):
        for j in range(i):
            if (bit >> j) & 1 and (bit >> i) & 1:
                dist = max(dist, D[i][j])
    dp[0][bit] = dist


def construct_dp():
    for k in range(1, K):
        for bit in range(1 << N):
            b = bit
            while b:
                dp[k][bit] = min(dp[k][bit], max(dp[k - 1][b], dp[0][bit - b]))
                b = (b - 1) & bit


construct_dp()
print(dp[K - 1][(1 << N) - 1])


"""
pypy,pythonだと厳しいやつ
"""
