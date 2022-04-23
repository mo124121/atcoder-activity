N, P = map(int, input().split())
dp = [[0] * (N + 10) for _ in range(N + 10)]
dp[0][0] = 1
for i in range(N):
    if i != 0:
        for j in range(N + 3):
            dp[i][j + 1] = (dp[i][j] + dp[i][j + 1]) % P
    for j in range(N):
        ways = dp[i][j] * (26 if i == 0 else 25) % P
        L, k = 1, 1
        while L <= N - j:
            R = min(L * 10, N - j + 3)
            di = k + 1
            dp[i + di][j + L] = (dp[i + di][j + L] + ways) % P
            dp[i + di][j + R] = (dp[i + di][j + R] - ways) % P
            L, k = L * 10, k + 1

print(sum([dp[i][N] for i in range(N)]) % P)


"""
1文字の時->1増える
2文字の時->同じ
3文字以上の時->N-2減る

N<3000
N**2*logN　あたりまではいけそう

dpっぽいはぽい
文字は増やした時の文字数、的な
dp[i][j]=i文字使って加工後にj文字になっているパターン数
遷移は同じ文字か違う文字か

桁上がりがあることを忘れていた

dp[i][j][k]=i文字使って加工後にj文字になっていて、最後の文字のカウント数がk個の時のパターン数

N**3じゃねーか

遷移する方向を考えなおしてみる
dp[i][j]=i文字使って加工後にj文字になっているパターン数
同じ文字が続けられるだけiを伸ばしていくというのは？
jの遷移は文字を変えるイメージ

あとは累積和とる、なお実装

"""
