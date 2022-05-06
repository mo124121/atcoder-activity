A, B, X = map(int, input().split())


def calc(n):
    return A * n + B * len(str(n))


l = 0
r = 10**9 + 1

while r - l > 1:
    m = (l + r) // 2
    v = calc(m)
    if v <= X:
        l = m
    else:
        r = m

print(l)
