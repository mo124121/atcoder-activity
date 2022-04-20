from bisect import bisect, bisect_left


N = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)

dp = set()
dp.add(0)
tmp = set()
for t in T:
    for d in dp:
        tmp.add(d + t)
    dp = dp.union(tmp)
    tmp.clear()

dp = list(dp)
dp.sort()

i = bisect_left(dp, (1 + dp[-1]) // 2)

print(dp[i])


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
bisect_leftと奇数の時の処理忘れてました

"""
