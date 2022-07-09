N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())) + [0]

prev = 0
ans = 0
for i in range(N + 1):
    ans += min(prev, A[i])
    A[i] = max(A[i] - prev, 0)
    ans += min(A[i], B[i])
    prev = max(B[i] - A[i], 0)

print(ans)
