N = int(input())
H = list(map(int, input().split()))

ret = 0

for h in H:
    if ret < h:
        ret = h
    else:
        break


print(ret)
