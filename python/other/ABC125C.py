from functools import lru_cache


N = int(input())
A = list(map(int, input().split()))


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


L = [0] * N
R = [0] * N
l = A[0]
for i in range(N - 1):
    l = gcd(l, A[i])
    L[i] = l
r = A[N - 1]
for i in range(N - 1, 0, -1):
    r = gcd(r, A[i])
    R[i] = r
ret = max(L[-2], R[1])
for i in range(1, N - 1):
    ret = max(ret, gcd(L[i - 1], R[i + 1]))
print(ret)
"""
最大公約数
N<10**5

ある要素を除いた最大公約数が答え、的な
左方向からの最大公約数をそれぞれ保存
逆からも保存
"""
