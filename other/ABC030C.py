from bisect import bisect_left


N, M = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ret = 0
t = 0
while True:
    s = bisect_left(A, t)
    if s == N:
        break
    t = A[s] + X

    s = bisect_left(B, t)
    if s == M:
        break
    t = B[s] + Y
    ret += 1
print(ret)

"""
二分探索で移動後の便を探す
もうなくなってたら終了

"""
