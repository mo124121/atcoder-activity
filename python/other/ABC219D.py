N = int(input())
X, Y = map(int, input().split())

INF = 10**18
dp = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    a, b = map(int, input().split())
    dp[i + 1][0][0] = 0
    for x in range(X + 1):
        nx = min(x + a, X)
        for y in range(Y + 1):
            ny = min(y + b, Y)
            dp[i + 1][x][y] = min(dp[i + 1][x][y], dp[i][x][y])
            dp[i + 1][nx][ny] = min(dp[i + 1][nx][ny], dp[i][nx][ny], dp[i][x][y] + 1)

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])

"""
DPっぽい

二つの変数の最大性をどう考えるか？
まあでもX,Yの数は知れているし、
ごり押しでいい気がする

dp[i][x][y]:i個目まで弁当を食べてx個とy個食べるときの弁当の最小値


"""
