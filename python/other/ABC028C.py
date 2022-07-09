from itertools import combinations


X = list(map(int, input().split()))

ret = []
for pat in combinations(X, 3):
    ret.append(sum(pat))
ret.sort(reverse=True)
print(ret[2])
