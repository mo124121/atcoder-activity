N = int(input())
T = [0] * N
K = [0] * N
A = [[] for _ in range(N)]

for i in range(N):
    tmp = input().split()
    T[i] = int(tmp[0])
    K[i] = int(tmp[1])
    for j in tmp[2:]:
        A[i].append(int(j))

from collections import deque

d = deque()
d.append(N)
ret = 0
seen = {}
while len(d):
    waza = d.pop()
    ret += T[waza - 1]
    for need in A[waza - 1]:
        if need not in seen:
            d.append(need)
            seen[need] = True

print(ret)
