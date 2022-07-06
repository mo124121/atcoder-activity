N = int(input())

ret = 0
for i in range(1, N + 1):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 8 and i % 2 == 1:
        ret += 1
print(ret)
