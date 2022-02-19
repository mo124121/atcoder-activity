x1, y1, x2, y2 = map(int, input().split())

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

seen = {}
for i in range(8):
    seen[(x1 + move_x[i], y1 + move_y[i])] = True

ret = False
for i in range(8):
    if (x2 + move_x[i], y2 + move_y[i]) in seen:
        ret = True

if ret:
    print("Yes")
else:
    print("No")
