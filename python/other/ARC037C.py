from bisect import bisect


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
        count += bisect(B, m // a)
    if count < K:
        l = m
    else:
        r = m
print(r)
