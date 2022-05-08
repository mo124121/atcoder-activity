import numpy as np

N = int(input())
MAX = 10000

in_A = np.zeros(MAX + 1, np.bool_)
for d in [6, 10, 15]:
    in_A[d::d] = 1

A = np.where(in_A)[0]
A[2], A[3] = A[3], A[2]  # avoid gcd(A) > 1
print(*A[:N])

# for debug
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = A[0]
for a in A:
    x = gcd(x, a)
print(x)

"""
最小公倍数を出すイメージ？

全体では最大公約数は1->互いに素なものが含まれる　1組以上
全ての組に関して、gcd>1 互いに素ではない
矛盾してない？

例題の約数列挙したらわかったが、
共有しない素数がそれぞれあるイメージ

とりあえず素数列を必要数生成して、
省く素数を1個ずつづらしていく

1万以下の制約
別に全部使う必要はない
2 3 5だけ使って、2だけ増やしていくとかでいい

あかんでかすぎる

×でなく足せば？

解説後
理解間違い（無限回）
"""
