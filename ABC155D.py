from bisect import bisect


def naive(N, K, A):
    B = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            B.append(A[i] * A[j])
    B.sort()
    return B[K - 1]


bisect


def count(N, A, x):
    tot = 0
    for i, a in enumerate(A):
        l = -1
        r = N
        if a < 0:
            while r - l > 1:
                m = (l + r) // 2
                if a * A[m] < x:
                    r = m
                else:
                    l = m
            tot += N - r
        else:
            while r - l > 1:
                m = (l + r) // 2
                if a * A[m] < x:
                    l = m
                else:
                    r = m
            tot += r
        if a**2 < x:
            tot -= 1
    tot //= 2
    return tot


def solve(N, K, A):
    A.sort()
    l = -(10**18) - 1
    r = 10**18 + 1
    while r - l > 1:
        m = (r + l) // 2
        if count(N, A, m) < K:
            l = m
        else:
            r = m
    return l


def submit():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, K, A))


submit()

test = [[4, 6, [1, 2, 3, 4]], [4, 4, [1, 2, 3, 4]], [4, 3, [3, 3, -4, -2]]]

for N, K, A in test:
    s = solve(N, K, A)
    g = naive(N, K, A)
    if s != g:
        print(N, K, *A, s, g)

"""
計算ができれば楽勝だが、
N<2*10**5

二分探索的にやっていく

解説後
k番目の数→x未満がk個未満であるxの最大値
重要な言い換え

解説はpypyでもTLEになるので書き換えが必要
"""
