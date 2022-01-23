N, T = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

total = sum(A)
if total <= T:
    print(0)
    exit()

C = [A[i] - B[i] for i in range(N)]
C.sort(reverse=True)

for i in range(N):
    total -= C[i]
    if total <= T:
        print(i + 1)
        exit()

print(-1)
