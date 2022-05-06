from collections import defaultdict, deque


N, M = map(int, input().split())

G = defaultdict(list)
for i in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

ret = 0
for i in range(1, N + 1):
    q = deque()
    seen = set()
    q.append(i)
    seen.add(i)
    while len(q):
        j = q.popleft()
        ret += 1
        for nxt in G[j]:
            if nxt not in seen:
                q.append(nxt)
                seen.add(nxt)
print(ret)
