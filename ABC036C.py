N = int(input())
A = []
for i in range(N):
    A.append(int(input()))


def compress(L):
    S = sorted(set(L))
    d = dict()
    i = 0
    for s in S:
        d[s] = i
        i += 1
    return i, S, d


n, S, d = compress(A)

for a in A:
    print(d[a])

"""
タイトルが座標圧縮
"""
