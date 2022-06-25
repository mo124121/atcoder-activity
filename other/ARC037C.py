from bisect import bisect, bisect_left


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
l = 0
r = 10**18 + 1

while r - l > 1:
    m = (l + r) // 2
    count = 0
    for a in A:
        sm = 0
        bg = N
        while bg - sm > 1:
            mi = (sm + bg) // 2
            if a * B[mi] <= m:
                sm = mi
            else:
                bg = mi
        count += sm
    if count <= K:
        l = m
    else:
        r = m
print(l)
