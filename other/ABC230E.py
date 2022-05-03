N = int(input())


def calc_sum(x):
    return x * (x + 1) // 2


ret = 0
i = 1
while True:
    ret += (N + i - 1) // i


"""
数え上げのsqrt(N)を狙うイメージ

ある時は同じ数字が並ぶ、その区間

"""
