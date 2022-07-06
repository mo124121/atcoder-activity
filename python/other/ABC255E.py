from collections import Counter


N, M = map(int, input().split())
S = list(map(int, input().split()))
X = set(map(int, input().split()))

A = [0]
for s in S:
    a = s - A[-1]
    A.append(a)
B = [[] for _ in range(2)]
for i, a in enumerate(A):
    B[i % 2].append(a)

elems = []
for i in range(N):
    for x in X:
        c = x - A[i]
        if i % 2 != 0:
            c *= -1
        elems.append(c)

occ_count = Counter(elems)

print(occ_count.most_common(1)[0][1])


"""
天才解法を眺める

"""
