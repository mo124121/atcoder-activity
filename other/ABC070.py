N = int(input())
T = [int(input()) for _ in range(N)]

import math

ret = 1


def lcm(a, b):
    return a * b // math.gcd(a, b)


for i in range(N):
    ret = lcm(ret, T[i])

print(ret)
