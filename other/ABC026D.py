from math import pi, sin


A, B, C = map(int, input().split())

e = 10 ** (-8)

l = 0
r = 10000


def f(x):
    return A * x + B * sin(C * x * pi)


v = 0
while abs(v - 100) > e:
    m = (r + l) / 2
    v = f(m)
    if v > 100:
        r = m
    else:
        l = m

print(f"{r:.20f}")
