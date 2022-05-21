N = int(input())

L = []
R = []
for _ in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        r -= 0.1
        l += 0.1
    L.append(l)
    R.append(r)

ret = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        l1, r1 = L[i], R[i]
        l2, r2 = L[j], R[j]
        if max(l1, l2) <= min(r1, r2):
            ret += 1
print(ret)
