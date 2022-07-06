N = int(input())
X = [0] * N
Y = [0] * N
H = [0] * N

HXY = []
for i in range(N):
    x, y, h = map(int, input().split())
    HXY.append((h, x, y))
HXY.sort(reverse=True)

for cx in range(101):
    for cy in range(101):
        ch = HXY[0][0] + abs(cx - HXY[0][1]) + abs(cy - HXY[0][2])

        flag = True
        for h, x, y in HXY[1:]:
            if max(ch - abs(x - cx) - abs(y - cy), 0) != h:
                flag = False
                break
        if flag:
            print(cx, cy, ch)
            exit()
