from bisect import bisect, bisect_left


N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

t = 0
ret = 0
while True:
    i = bisect_left(A, t)
    if i == N:
        break
    t = A[i] + X
    i = bisect_left(B, t)
    if i == M:
        break
    t = B[i] + Y
    ret += 1
print(ret)
