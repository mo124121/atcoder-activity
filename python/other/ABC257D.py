from bisect import bisect
from collections import deque


N = int(input())

xyP = []
for i in range(N):
    xyP.append(list(map(int, input().split())))

D = []
for i, (x1, y1, _) in enumerate(xyP):
    D.append(list())
    for j, (x2, y2, _) in enumerate(xyP):
        D[-1].append((abs(x1 - x2) + abs(y1 - y2), j))
    D[-1].sort()


l = 0
r = 10**10 + 1
while r - l > 1:
    m = (r + l) // 2
    lim = []
    flag = False
    for i in range(N):
        lim.append(bisect(D[i], (m * xyP[i][2], 10**3)))
    for i in range(N):
        seen = set()
        q = deque()
        q.append(i)
        seen.add(i)
        while q:
            node = q.popleft()
            for _, nxt in D[node][: lim[node]]:
                if nxt not in seen:
                    q.append(nxt)
                    seen.add(nxt)
        if len(seen) == N:
            flag = True
            break
    if flag:
        r = m
    else:
        l = m

print(r)
