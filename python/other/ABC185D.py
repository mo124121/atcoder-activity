N, M = map(int, input().split())
A = list(map(int, input().split()))
A = [0] + A + [N + 1]
A.sort()

k = N + 1
B = []

for i in range(M + 1):
    diff = A[i + 1] - A[i] - 1
    if diff > 0:
        k = min(k, diff)
        B.append(diff)


ret = 0
for b in B:
    ret += (b + k - 1) // k

print(ret)
