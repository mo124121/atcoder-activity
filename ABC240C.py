N, X = map(int, input().split())

dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    a, b = map(int, input().split())
    for j in range(X + 1):
        if a <= j and dp[i][j - a]:
            dp[i + 1][j] = True
        if b <= j and dp[i][j - b]:
            dp[i + 1][j] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")
