X = int(input())

if X == 1:
    print(1)
    exit()

ret = 0
for i in range(2, 34):
    for p in range(2, 10):
        if pow(i, p) > X:
            break
        ret = max(ret, pow(i, p))

print(ret)
