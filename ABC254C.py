N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [[] for _ in range(K)]
for i, a in enumerate(A):
    B[i % K].append(a)

for i in range(K):
    B[i].sort()

C = []
for i in range(N):
    C.append(B[i % K][i // K])

if sorted(A) == C:
    print("Yes")
else:
    print("No")
