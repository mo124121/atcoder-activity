N = int(input())


def calc_sum(x):
    return x * (x + 1) // 2


i = 1
ret = 0
while i**2 <= N:
    ret += (N // i - i) * 2 + 1
    i += 1

print(ret)

"""
数え上げのsqrt(N)を狙うイメージ

ある時は同じ数字が並ぶ、その区間

R-L=i*(R*(R+1)//2 - L*(L+1)//2)

解説後
そもそもfloorとceilを間違えてしっちゃかめっちゃか
グラフを書くとわかりやすい
sqrtのオーダでたたける


"""
