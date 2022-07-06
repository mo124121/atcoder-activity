from itertools import combinations


N, M, P, Q, R = map(int, input().split())
XYZ = []
for _ in range(R):
    XYZ.append(tuple(map(int, input().split())))
ret = 0
for pat in combinations(range(1, N + 1), P):
    score = [0] * (M + 1)
    pat = set(pat)
    for x, y, z in XYZ:
        if x in pat:
            score[y] += z
    score.sort(reverse=True)
    ret = max(ret, sum(score[:Q]))
print(ret)
