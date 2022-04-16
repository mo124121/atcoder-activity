# import numpy as np

from decimal import Decimal


s = input().split()
p = Decimal(s[0])
n = int(s[1])

# 　状態遷移確率の計算
P = [Decimal(0) for _ in range(62)]
P[0] = p
for i in range(61):
    P[i + 1] = 2 * P[i] * (1 - P[i])
ret = Decimal(0)
for i in range(62):
    if (n >> i) & 1 == 1:
        q = P[i]
        ret = ret * q + (1 - ret) * q

print("{:.7f}".format(ret))
"""
考察
見るからに確率DP

n<10**18

これで回すことはできない、どうするか？

最終的に.5に収束はしそう
ただ例題2的にまあまあ回さないといけない

1回のでる確率p
2回ででる確率p*(1-p)+(1-p)*p=p2
4回の出る確率p2*(1-p2)+(1-p2)*p2=p4

倍々で確率テーブルを持つ作戦は悪くないはずだが、誤差がひどい
高々10**-10なら、intで管理してしまう、とうのは？できる？
大したループ数ではないので、多倍長でもなんとかなるはず　->あかんかったわ

doubleは16桁しか持てないので、
10桁×10桁は事故る→それぐらいの桁を何とかする必要あり


解説

float128とかいう力技

そもそも合わないからなんか間違えてる

"""
