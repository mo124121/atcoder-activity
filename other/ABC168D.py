from collections import defaultdict, deque
from email.policy import default


N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ret = [0] * (N + 1)
ret[0] = 1

dq = deque()
dq.append(1)

while len(dq):
    room = dq.popleft()
    for neibor in G[room]:
        if ret[neibor] == 0:
            ret[neibor] = room
            dq.append(neibor)

print("Yes")
print(*ret[2:], sep="\n")
