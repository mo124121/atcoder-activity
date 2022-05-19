N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
l = -(10**18) - 1
r = 10**18 + 1


def count(x):
    k = 0
    for a in A:
        l = 0
        r = len(A)
        while r - l > 1:
            m = (r + l) // 2
            if a * A[m] < x:
                l = m
            else:
                r = m
        if a * a < a * A[l]:
            k -= 1
        k += l

    return k


while r - l > 1:
    m = (r + l) // 2
    if count(m) < K:
        l = m
    else:
        r = m

print(l)


"""
計算ができれば楽勝だが、
N<2*10**5

二分探索的にやっていく

"""
