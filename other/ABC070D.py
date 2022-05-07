from collections import defaultdict, deque


N = int(input())
from collections import defaultdict

G = defaultdict(list)
for i in range(N - 1):
    a, b, cn = map(int, input().split())
    G[a].append((b, cn))
    G[b].append((a, cn))

Q, K = map(int, input().split())

C = [0] * (N + 1)
q = deque()
q.append((K, 0))
seen = set()
while len(q):
    node, cost = q.popleft()
    C[node] = cost
    for nxt, cn in G[node]:
        if nxt not in seen:
            seen.add(nxt)
            q.append((nxt, cn + cost))
for i in range(Q):
    x, y = map(int, input().split())
    print(C[x] + C[y])

"""
緑後半はグラフが多いな
Kを頂点にして考えるのがよい

"""
