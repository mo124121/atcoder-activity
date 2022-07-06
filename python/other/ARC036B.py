N = int(input())
INF = 10**10
H = [INF] + [int(input()) for _ in range(N)] + [INF]

asc = [0] * (N + 2)
for i in range(N + 1):
    if H[i] < H[i + 1]:
        asc[i + 1] = asc[i] + 1

des = [0] * (N + 2)
for i in reversed(range(N + 1)):
    if H[i] > H[i + 1]:
        des[i] = des[i + 1] + 1

ret = 0
for i in range(1, N + 1):
    ret = max(ret, asc[i] + des[i] + 1)

print(ret)
