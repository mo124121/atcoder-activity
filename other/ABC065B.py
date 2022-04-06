N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input()) - 1
r = 0
for i in range(N):
    r = A[r]
    if r == 1:
        print(i + 1)
        exit()
print(-1)
