N, X = map(int, input().split())
A = list(map(int, input().split()))
ret = 0
for i in range(N - 1):
    c = A[i] + A[i + 1]
    if c <= X:
        continue
    if c - X <= A[i + 1]:
        A[i + 1] -= c - X
    else:
        A[i] -= c - X - A[i + 1]
        A[i + 1] = 0
    ret += c - X
print(ret)

"""
大きいほうから削るのが吉
端より真ん中

貪欲にやっていく
"""
