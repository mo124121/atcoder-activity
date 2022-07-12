N, K = map(int, input().split())
A = list(map(int, input().split()))
AA = []
for l in range(N):
    a = 0
    for r in range(l, N):
        a += A[r]
        AA.append(a)
ans = 0
for bit in reversed(range(40)):
    B = []
    for a in AA:
        if (a >> bit) & 1:
            B.append(a)
    if len(B) >= K:
        ans += 1 << bit
        AA = B
print(ans)
