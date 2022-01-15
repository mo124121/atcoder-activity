N = int(input())
A = []
B = []
a = 0
b = 0
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        a += p
    else:
        b += p
    A.append(a)
    B.append(b)
A += [0]
B += [0]
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print((A[r - 1] - A[l - 2]), (B[r - 1] - B[l - 2]))
