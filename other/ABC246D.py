N = int(input())


def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


ret = 0
b = 0
for a in range(10**6 + 1):
    ret = calc(a, b)
    if N <= ret:
        break

while a >= 0:
    a -= 1
    flag = True
    for b in range(b, a + 1):
        r = calc(a, b)
        if N <= r:
            ret = min(ret, r)
            break

print(ret)
