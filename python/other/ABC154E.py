from functools import lru_cache


N = int(input())  # 多倍長
K = int(input())


@lru_cache(maxsize=None)
def rec(n, k):
    if n < 10:
        if k == 0:
            return 1
        if k == 1:
            return n
        return 0

    q, r = divmod(n, 10)
    ret = 0
    if k > 0:
        ret += r * rec(q, k - 1)
        ret += (9 - r) * rec(q - 1, k - 1)
    ret += rec(q, k)

    return ret


print(rec(N, K))

"""
Kの大きさ？で再帰的構造がありそう

最大値をとっていく時とそうじゃないとき
もっというと上3桁を使う時とそうじゃないとき -> 1個しかないのでは？

2項係数で考える感じ？

面倒なので場合分けしていく

0999
8***
98**
990*
99*0

数字合わないので解説見る
桁DPとな…

その前に再帰で解いてみる

"""
