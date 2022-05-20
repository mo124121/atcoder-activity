def naive(N, K, A):
    B = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            B.append(A[i] * A[j])
    B.sort()
    return B[K - 1]


def getMinus(pl, mi, l):
    j = 0
    ret = 0
    for m in mi:
        while j < len(pl) and l < m * pl[j]:
            j += 1
        ret += len(pl) - j
    return ret


def getPlus(pl, mi, l):

    ret = 0
    mi = list(reversed(mi))
    n = len(mi)
    j = n - 1
    for i in range(n):
        while i < j and l < mi[i] * mi[j]:
            j -= 1
        ret += max(0, j - i)

    n = len(pl)
    j = n - 1
    for i in range(n):
        while i < j and l < pl[i] * pl[j]:
            j -= 1
        ret += max(0, j - i)
    return ret


def getCount(pl, mi, zero, l):
    ret = getMinus(pl, mi, min(l, -1))
    if 0 <= l:
        ret += zero
    if 0 < l:
        ret += getPlus(pl, mi, l)
    return ret


def solve(N, K, A):
    A.sort()

    mi = []
    pl = []
    for i in range(N):
        if A[i] < 0:
            mi.append(A[i])
        elif A[i] > 0:
            pl.append(A[i])
    zero = 0
    for a in A:
        if a == 0:
            zero += 1
    zero = zero * (N - zero) + zero * (zero - 1) // 2

    ng = -(10**18) - 1
    ok = 10**18 + 1
    while ok - ng > 1:
        m = (ok + ng) // 2
        if K <= getCount(pl, mi, zero, m):
            ok = m
        else:
            ng = m

    return ok


def submit():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, K, A))


submit()

# test = [[4, 6, [1, 2, 3, 4]], [4, 4, [1, 2, 3, 4]], [4, 3, [3, 3, -4, -2]]]

# for N, K, A in test:
#     s = solve(N, K, A)
#     g = naive(N, K, A)
#     if s != g:
#         print(N, K, *A, s, g)

"""
計算ができれば楽勝だが、
N<2*10**5

二分探索的にやっていく

解説後
k番目の数→x未満がk個未満であるxの最大値
重要な言い換え

解説はpypyでもTLEになるので書き換えが必要
"""
