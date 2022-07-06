x, y, W = input().split()
x = int(x) - 1
y = int(y) - 1
C = [input() for _ in range(9)]

mv = [0, 0]
if "R" in W:
    mv[1] = 1
elif "L" in W:
    mv[1] = -1
if "U" in W:
    mv[0] = -1
elif "D" in W:
    mv[0] = 1

ret = C[y][x]

for i in range(3):
    x = x + mv[1]
    y = y + mv[0]
    if x < 0:
        x = 1
        mv[1] = 1
    if 8 < x:
        x = 7
        mv[1] = -1
    if y < 0:
        y = 1
        mv[0] = 1
    if 8 < y:
        y = 7
        mv[0] = -1
    ret += C[y][x]
print(ret)


"""
ただただ面倒


"""
