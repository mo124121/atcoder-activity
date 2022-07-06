from collections import deque


S = input()
K = int(input())

S = deque(S)
q = deque()
total = 0
ret = 0
while S:
    c = S.popleft()
    q.append(c)
    total += 1
    if c == ".":
        K -= 1
    while K < 0:
        cq = q.popleft()
        if cq == ".":
            K += 1
        total -= 1
    ret = max(ret, total)

print(ret)
