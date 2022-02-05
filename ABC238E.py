from collections import defaultdict, deque

N, Q = map(int, input().split())
l = [0] * Q
r = [0] * Q

G = defaultdict(list)

for i in range(Q):
    l, r = map(int, input().split())
    G[l - 1].append(r)
    G[r].append(l - 1)

q = deque()
q.append(0)
seen = {0: True}
while len(q):
    node = q.pop()
    for neibor in G[node]:
        if neibor == N:
            print("Yes")
            exit()
        if neibor not in seen:
            seen[neibor] = True
            q.append(neibor)

print("No")
