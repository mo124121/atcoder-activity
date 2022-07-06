N, D = map(int, input().split())
ret = 0
for _ in range(N):
    X, Y = map(int, input().split())
    if D ** 2 >= X ** 2 + Y ** 2:
        ret += 1
print(ret)
