N, x, y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ok = A[0]
ng = A[-1] + 1

while ng - ok > 1:
    mid = (ok + ng) // 2
    count = 0
    for a in A:
        if a < mid:
            count += -((mid - a + x - 1) // x)
        elif a > mid:
            count += (a - mid) // y
    if count >= 0:
        ok = mid
    else:
        ng = mid
print(ok)
