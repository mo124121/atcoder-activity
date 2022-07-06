N = int(input())

ret = 0
tmp = [[0] * 10 for _ in range(10)]

for i in range(1, N + 1):
    st = int(str(i)[0])
    end = i % 10
    tmp[st][end] += 1

ret = 0

for i in range(1, 10):
    for j in range(1, 10):
        ret += tmp[i][j] * tmp[j][i]

print(ret)
