N, K = map(int, input().split())

ret = 0
for i in range(1, N + 1):
    for j in range(1, K + 1):
        ret += i * 100 + j

print(ret)
