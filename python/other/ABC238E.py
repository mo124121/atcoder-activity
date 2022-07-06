N, Q = map(int, input().split())
from collections import defaultdict, deque

G = defaultdict(list)
for i in range(Q):
    l, r = map(int, input().split())
    G[l - 1].append(r)
    G[r].append(l - 1)

q = deque()
q.append(0)
seen = set()
seen.add(0)
while q:
    node = q.popleft()
    if node == N:
        print("Yes")
        exit()
    for nxt in G[node]:
        if nxt not in seen:
            seen.add(nxt)
            q.append(nxt)
print("No")
