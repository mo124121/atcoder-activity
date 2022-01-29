N = int(input())
A = list(map(int, input().split()))

L = 0
R = 10 ** 9 + 1

while R - L > 0.5 * 10 ** -3:
    M = (R + L) / 2
    B = [A[i] - M for i in range(N)]
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(N):
        dp[i + 1][0] = dp[i][1]
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + B[i]

    if max(dp[N]) > 0:
        L = M
    else:
        R = M
print(L)

L, R = 0, 10 ** 9 + 1
while L < R:
    M = (L + R + 1) >> 1
    B = [-1] * N
    for i in range(N):
        if A[i] >= M:
            B[i] = 1
    dp = [[0, 0] for _ in range(N + 1)]

    for i in range(N):
        dp[i + 1][0] = dp[i][1]
        dp[i + 1][1] = max(dp[i][0], dp[i][1]) + B[i]

    if max(dp[N]) > 0:
        L = M
    else:
        R = min(R - 1, M)
print(L)
