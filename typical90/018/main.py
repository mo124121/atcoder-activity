import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

for i in range(Q):
    rad = math.radians(360 * E[i] / T)
    y = -L / 2 * math.sin(rad)
    z = L / 2 * (1 - math.cos(rad))
    ret = math.degrees(math.asin(z / (X ** 2 + (y - Y) ** 2 + z ** 2) ** 0.5))
    print(ret)
