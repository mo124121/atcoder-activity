L, R = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


ret = 0
for l in range(L, R):
    if R - l < ret:
        break
    for r in range(R, L, -1):
        tmp = r - l
        if gcd(l, r) == 1:
            break
        if ret > tmp:
            break
    if ret < tmp:
        ret = tmp

print(ret)
