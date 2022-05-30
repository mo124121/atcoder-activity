N, M = map(int, input().split())


ret = []
if M == 0:
    for i in range(N):
        ret.append((0, 1))
elif M < 0:
    for i in range(N - 1):
        ret.append((-(2 * i + 1), -(2 * i + 2)))
    ret.append((-M * 2, 0))
else:
    for i in range(N - 1):
        ret.append((2 * i + 1, 2 * i + 2))
    ret.append((0, M * 2))

for r in ret:
    print(*r)
