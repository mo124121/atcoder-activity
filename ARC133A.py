N = int(input())
A = list(map(int, input().split()))

count = [0] * (N + 1)
ret = [N + 1]

target = A[-1]
for i in range(N - 1):
    if A[i] > A[i + 1]:
        target = A[i]
        break

ret = []
for a in A:
    if a != target:
        ret.append(a)


print(*ret)
