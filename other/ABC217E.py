from collections import deque
from heapq import heappop, heappush


Q = int(input())

waiting = deque()
h = []
ret = []
for i in range(Q):
    line = input()
    c = int(line[0])

    if c == 1:
        waiting.append(int(line[2:]))
    if c == 2:
        if len(h):
            ret.append(heappop(h))
        else:
            ret.append(waiting.popleft())
    if c == 3:
        while len(waiting):
            heappush(h, waiting.popleft())

print(*ret, sep="\n")
