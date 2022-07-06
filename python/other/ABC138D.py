from collections import defaultdict, deque


N, Q = map(int, input().split())

G = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

C = defaultdict(int)
for i in range(Q):
    p, x = map(int, input().split())
    C[p] += x

q = deque()
q.append((1, C[1]))
seen = set()
ret = [0] * (N + 1)
while len(q):
    node, cost = q.popleft()
    ret[node] = cost
    seen.add(node)
    for neibor in G[node]:
        if neibor not in seen:
            q.append((neibor, cost + C[neibor]))


print(*ret[1:])
