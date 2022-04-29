from collections import defaultdict, deque


N, Q = map(int, input().split())

G = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
P = [0] * (N + 1)
for i in range(Q):
    p, x = map(int, input().split())
    P[p] += x

ret = [0] * (N + 1)

q = deque()
q.append((1, P[1]))
seen = set()
seen.add(1)

while len(q):
    node, count = q.popleft()
    ret[node] = count
    for child in G[node]:
        if child not in seen:
            q.append((child, count + P[child]))
            seen.add(child)

print(*ret[1:])


"""
N<10**5
幅探索しつつ、足してったらいいのでは

AC
解説後
いもすといわれればいもす
"""
