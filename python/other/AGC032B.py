N = int(input())

NG = N
if N % 2 == 1:
    NG -= 1

ret = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j <= i or j == NG:
            continue
        ret.append((i, j))
    NG -= 1

print(len(ret))
for p in ret:
    print(*p)
