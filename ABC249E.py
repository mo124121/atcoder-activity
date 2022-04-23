N, P = map(int, input().split())
if N <= 2:
    print(0)
    exit()


dp = [[0] * N for _ in range(N + 1)]
dp[0][0] = 1
dp[1][0] = -1

for j in range(N):
    if j == 0:
        pat = 26
    else:
        pat = 25
    for i in range(N):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= P
    for i in range(N):
        for k in range(1, 5):
            if i + 10 ** (k - 1) <= N and j + 1 + k < N:
                dp[i + 10 ** (k - 1)][j + 1 + k] += dp[i][j] * pat
                dp[i + 10 ** (k - 1)][j + 1 + k] %= P
                if i + 10**k < N + 1:
                    dp[i + 10**k][j + 1 + k] -= dp[i][j] * pat


print(sum(dp[N]) % P)


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
