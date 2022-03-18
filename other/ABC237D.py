from collections import deque


N = int(input())
S = input()

dq = deque()
dq.append(N)
for i in range(N - 1, -1, -1):
    c = S[i]
    if c == "L":
        dq.append(i)
    else:
        dq.appendleft(i)
    prev = c
print(*list(dq))
