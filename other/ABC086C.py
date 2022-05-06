N = int(input())
pt = 0
px = 0
py = 0
ret = "Yes"
for i in range(N):
    t, x, y = map(int, input().split())
    d = abs(x - px) + abs(y - py)
    dt = t - pt
    if d > dt:
        ret = "No"
    if (dt - d) % 2 != 0:
        ret = "No"
    pt, px, py = t, x, y
print(ret)
