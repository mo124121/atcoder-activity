N = int(input())
A = list(map(int, input().split()))
B = [-1] * (N + 1)
for i in range(N, 0, -1):
    r = 0
    for j in range(i * 2, N + 1, i):
        r += B[j]
    if r % 2 == A[i - 1]:
        B[i] = 0
    else:
        B[i] = 1


ret = []
for i in range(N + 1):
    if B[i] == 1:
        ret.append(i)

print(len(ret))
if len(ret):
    print(*ret)
