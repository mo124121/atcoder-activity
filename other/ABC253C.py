from collections import Counter
from heapq import heappop, heappush


Q = int(input())
hs = []
hl = []
count = Counter()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        heappush(hs, x)
        heappush(hl, -x)
        count[x] += 1
    elif q[0] == 2:
        x = q[1]
        c = q[2]
        count[x] = max(0, count[x] - c)
    else:
        while count[hs[0]] == 0:
            heappop(hs)
        while count[-hl[0]] == 0:
            heappop(hl)
        print(-hl[0] - hs[0])

"""
heap解法
"""
