N = int(input())


def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


for ab in range(10**6 + 1):
    if N <= 4 * ab**3:
        break

ret = 4 * ab**3
for a in range(ab, 2 * ab + 1):

    l = -1
    r = a + 1
    m = (l + r) // 2
    while l < m:
        t = calc(a, m)
        if t < N:
            l = m
        else:
            r = m
        m = (l + r) // 2
    ret = min(ret, calc(a, r))

    if m == -1:
        break

print(ret)
