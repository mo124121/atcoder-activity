import sys

N = int(input())

D = []
for i in range(2, N + 1):
    print("? {} {}".format(1, i))
    sys.stdout.flush()
    dist = int(input())
    D.append((dist, i))
D.sort()
_, j = D[-1]

ret = 0
for i in range(1, N + 1):
    if i == j:
        continue
    print("? {0} {1}".format(j, i))
    sys.stdout.flush()
    dist = int(input())
    ret = max(dist, ret)
print("!", ret)
