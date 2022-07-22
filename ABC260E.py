N, M = map(int, input().split())
from collections import defaultdict, deque

G = defaultdict(list)
for i in range(N):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

G2 = {}
for i in range(1, M + 1):
    if i in G:
        G2[i] = (min(G[i]), max(G[i]))
    else:
        G2[i] = (M, 1)


ret = [0] * (M + 1)
seen = set()


q = deque()
q.append((1, M))
while q:
    s, t = q.pop()
    if (s, t) in seen:
        continue
    seen.add((s, t))
    ret[t - s + 1] += 1
    if s == t:
        continue
    if s + 1 <= G2[s][0] and G2[s][1] <= t:
        q.append((s + 1, t))
    if s <= G2[t][0] and G2[t][1] <= t - 1:
        q.append((s, t - 1))

print(*ret[1:])


"""
方針誤りなり
"""
