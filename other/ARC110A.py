N = int(input())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


ret = 1
for i in range(2, N + 1):
    r = gcd(ret, i)
    ret *= i // r


print(ret + 1)
# for debug
for i in range(2, N + 1):
    print(i, (ret + 1) % i)
print(len(str(ret + 1)), ret + 1 < 10**13)
