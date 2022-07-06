N = int(input())


def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


ret = 0
for a in range(10**6 + 1):
    ret = calc(a, a)
    if N <= ret:
        break

b = a
while a <= 10**6 + 1:
    while b >= 0:
        r = calc(a, b)
        if N <= r:
            ret = min(ret, r)
        else:
            break
        b -= 1
    a += 1

print(ret)
