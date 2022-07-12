from collections import defaultdict
from heapq import heappop, heappush


N, M = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort(reverse=True)

h = []
ans = 0
for d in range(M - 1, -1, -1):
    while AB and AB[-1][0] + d <= M:
        _, b = AB.pop()
        heappush(h, -b)
    if h:
        ans += -heappop(h)


print(ans)
