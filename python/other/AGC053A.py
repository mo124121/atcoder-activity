N = int(input())
S = input()
A = list(map(int, input().split()))

k = min([abs(A[i] - A[i + 1]) for i in range(N)])

print(k)
for j in range(k):
    r = []
    for l in range(N + 1):
        r.append(A[l] // k + int(A[l] % k > j))
    print(*r)
