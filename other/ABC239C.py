x1, y1, x2, y2 = map(int, input().split())

mvs = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

for mvx1, mvy1 in mvs:
    for mvx2, mvy2 in mvs:
        if (x1 + mvx1, y1 + mvy1) == (x2 + mvx2, y2 + mvy2):
            print("Yes")
            exit()

print("No")
