N = int(input())
S = input()

from collections import deque

deq = deque()

deq.append(N)
for i in reversed(range(N)):
    if S[i] == "R":
        deq.appendleft(i)
    else:
        deq.append(i)

print(*deq)
