N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = max(A) + 1

while r - l > 1:
    m = (r + l) // 2
    k = K
    for a in A:
        k -= (a - 1) // m

    if k >= 0:
        r = m
    else:
        l = m

print(r)
