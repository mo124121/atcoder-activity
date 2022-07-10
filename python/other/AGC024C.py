N = int(input())
A = [int(input()) for _ in range(N)] + [0]

ret = 0
for i in reversed(range(N)):
    if A[i + 1] - A[i] > 1 or A[i] > i:
        print(-1)
        exit()
    if A[i + 1] - A[i] != 1:
        ret += A[i]
print(ret)
