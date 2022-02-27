A1, A2, A3 = map(int, input().split())

X = 2 * A2 - A1 - A3

ret = 0
if X < 0:
    ret += abs(X) // 2
    X += abs(X) // 2 * 2


if X > 0:
    ret += X
elif X == -1:
    ret += 2
else:
    pass
print(ret)
