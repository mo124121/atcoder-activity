H, W = map(int, input().split())
R, C = map(int, input().split())
ret = 4
if R == 1:
    ret -= 1
if R == H:
    ret -= 1
if C == 1:
    ret -= 1
if C == W:
    ret -= 1
print(ret)
