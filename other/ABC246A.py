from collections import defaultdict

X = defaultdict(int)
Y = defaultdict(int)
for i in range(3):
    x, y = map(int, input().split())
    if x in X:
        del X[x]
    else:
        X[x] += 1
    if y in Y:
        del Y[y]
    else:
        Y[y] += 1

retx = 0
rety = 0

for k in X.keys():
    retx = k

for k in Y.keys():
    rety = k

print(retx, rety)
