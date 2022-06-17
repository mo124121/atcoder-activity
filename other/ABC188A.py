XY = list(map(int, input().split()))
XY.sort()
if XY[1] - XY[0] < 3:
    print("Yes")
else:
    print("No")
