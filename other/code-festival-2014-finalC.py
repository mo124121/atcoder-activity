A = int(input())

for i in range(10, 100001):
    ds = str(i)
    r = 0
    for d in ds:
        r *= i
        r += int(d)
    if r == A:
        print(i)
        exit()
print(-1)
