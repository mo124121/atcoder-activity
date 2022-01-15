N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(Q):
    x = int(input())
    ok = N
    ng = -1
    while (ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] >= x:
            ok = mid
        else:
            ng = mid
    print(N - ok)
