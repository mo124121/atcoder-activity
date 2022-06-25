N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))


for l in L:
    l -= 1
    if A[l] != N and A[l] + 1 not in A:
        A[l] += 1

print(*A)
