L, R = map(int, input().split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


ret = 0
l = L
while ret < R - l:
    r = R
    while True:
        if 1 == gcd(l, r):
            ret = max(ret, r - l)
            break
        else:
            r -= 1
    l += 1

print(ret)
