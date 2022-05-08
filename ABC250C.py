N, Q = map(int, input().split())

A = [i + 1 for i in range(N)]
pos = {}
for i, a in enumerate(A):
    pos[a] = i

for _ in range(Q):
    x = int(input())
    i = pos[x]
    if i == N - 1:
        j = i - 1
    else:
        j = i + 1
    pos[x] = j
    pos[A[j]] = i
    A[i], A[j] = A[j], A[i]


print(*A)
