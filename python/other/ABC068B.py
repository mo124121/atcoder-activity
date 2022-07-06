N = int(input())

ret = 1
for i in range(10):
    if ret * 2 > N:
        break
    ret *= 2
print(ret)
