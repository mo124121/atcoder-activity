N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ret = 0
for i in range(N):
    tmp = C
    for j in range(M):
        tmp += A[i][j] * B[j]
    if tmp > 0:
        ret += 1
print(ret)
