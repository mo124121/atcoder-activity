N = int(input())
XY = []
for i in range(N):
    XY.append(tuple(map(int, input().split())))

ret = 0
for xi, yi in XY:
    for xj, yj in XY:
        ret = max(ret, ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5)
print(f"{ret:.5f}")
