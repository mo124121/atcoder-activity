a, b, c = map(int, input().split())


if c - b - a >= 0 and 4 * a * b < (c - a - b) * (c - a - b):
    print("Yes")
else:
    print("No")

"""
リベンジ
rt(a)+rt(b)<rt(c)
a+2*rt(ab)+b<c
4*ab<(c-a-b)**2

"""
