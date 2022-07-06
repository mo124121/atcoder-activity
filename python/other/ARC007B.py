N, M = map(int, input().split())

A = list(range(N + 1))

D = [int(input()) for _ in range(M)]
now = {}
for i in range(N + 1):
    now[i] = i

for d in D:
    j = now[d]
    A[0], A[j] = A[j], A[0]
    now[A[j]] = j
    now[A[0]] = 0

print(*A[1:], sep="\n")
