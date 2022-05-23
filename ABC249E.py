N, P = map(int, input().split())

dp = [[0] * (N + 2) for _ in range(N + 5)]
dp[0][0] = 1

for i in range(N):
    if i == 0:
        way = 26
    else:
        way = 25
    for j in range(N):
        ways = dp[i][j] * way
        for d in range(4):
            if j + 10**d > N:
                break
            dp[i + 2 + d][j + 10**d] += ways
            dp[i + 2 + d][j + 10**d] %= P
            e = j + 10 ** (d + 1)
            if e <= N + 1:
                dp[i + 2 + d][e] -= ways
    for j in range(N):
        dp[i + 1][j + 1] += dp[i + 1][j]
        dp[i + 1][j + 1] %= P
ret = 0
for i in range(2, N):
    ret += dp[i][N]
    ret %= P

print(ret)

"""
解き方は忘れておる
DPで殴れるか？
N<3000

同じ文字を伸ばす場合と違う文字を伸ばす場合のパターン分け
ああああ思い出した累積和や
桁が上がるのがミソ

dp[i][j]:変換後i文字になる変換前j文字の文字列の個数
数字4文字分はみ出るからdp表は4文字多くする　今理解した
桁が上がるところだけ記載するようにして、
適宜累積和する

"""
