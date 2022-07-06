N, P = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    # 食べたとき
    dp[i + 1][1 - A[i] % 2] += dp[i][1]
    dp[i + 1][0 - A[i] % 2] += dp[i][0]
    # 食べなかったとき
    dp[i + 1][1] += dp[i][1]
    dp[i + 1][0] += dp[i][0]

ret = dp[i + 1][P]
print(ret)


"""
dp[i][p]=i個目の袋までpになっている時のパターンの数
全部食べても全部たべなくてもダメ　-> そのケースはそれぞれ一つなので最後に消す x 誤読　全部ためても「かまわない」

解説後
どっち選んでも遷移同じだから2**N-1でいい

"""
