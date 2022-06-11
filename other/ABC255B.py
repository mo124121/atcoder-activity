N, K = map(int, input().split())
A = list(map(int, input().split()))
A = set(A)
Xlight = []
Ylight = []
Xno = []
Yno = []
for i in range(N):
    x, y = map(int, input().split())
    if i + 1 in A:
        Xlight.append(x)
        Ylight.append(y)
    else:
        Xno.append(x)
        Yno.append(y)

ret = 0
for x, y in zip(Xno, Yno):
    r = 10**18
    for x2, y2 in zip(Xlight, Ylight):
        r = min(((x - x2) ** 2 + (y - y2) ** 2) ** 0.5, r)
    ret = max(r, ret)
print("{:.8f}".format(ret))
