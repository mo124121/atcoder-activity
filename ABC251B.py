N, W = map(int, input().split())
A = list(map(int, input().split()))

ret = set()
for i in range(N):
    ret.add(A[i])
    for j in range(N):
        if i == j:
            continue
        ret.add(A[i] + A[j])
        for k in range(N):
            if i == k or j == k:
                continue
            ret.add(A[i] + A[j] + A[k])
r = 0
for i in ret:
    if i <= W:
        r += 1
print(r)
