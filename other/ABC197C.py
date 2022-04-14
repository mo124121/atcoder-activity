from itertools import product


N = int(input())
A = list(map(int, input().split()))
ret = 1 << 31
for pat in product((True, False), repeat=N - 1):
    rs = []
    r = A[0]
    for i, p in enumerate(pat):
        if p:
            r |= A[i + 1]
        else:
            rs.append(r)
            r = A[i + 1]
    c = r
    for r in rs:
        c ^= r
    ret = min(ret, c)
print(ret)

"""
考察

N<20 -> 2^20 1000^2 10**6
全探索
(A1|A2)^(A3)

"""
