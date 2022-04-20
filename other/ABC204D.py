from bisect import bisect, bisect_left


N = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)
T_sum = sum(T)
T_max = max(T)
INF = T_sum
dp = [[INF] * (T_sum + T_max + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for t in range(T_sum + 1):
        dp[i + 1][t + T[i]] = min(dp[i + 1][t + T[i]], dp[i][t])
        dp[i + 1][t] = min(dp[i + 1][t], dp[i][t] + T[i])

ret = INF
for t in range(T_sum + 1):
    ret = min(ret, max(t, dp[N][t]))

print(ret)
"""
見たことある感
貪欲法でできるルールを設定できるか？

求める答えとして、
二つの袋ができるだけ差が小さくなるように中身を分けるイメージ

大きいのから順に空いてるところに割り振ればよさそう
降順ソートで貪欲
->はいWA

どうするか？

いったん立ち戻る
パターンとしては2^N
全探索は間に合わない

N*T<100*10**3
とりうる値の範囲が狭い dpでとりうる値を探す
sum(T)//2に一番近くて最も大きいものが答え
->はいWA　なんで？（おこ）

解説後
bisect_leftと奇数の時の処理忘れてました

上記は部分和問題への帰着
別解としてhamayanhamayan氏のdpも面白そう
そもそもメモる必要もないのでdpでもないくさい

"""
