N, M = map(int, input().split())
MOD = 10**9 + 7
from collections import defaultdict, deque

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

count = [0] * (N + 1)
count[1] = 1
seen = {}
seen[1] = 0
parent = set()
parent.add(1)
q = deque()
q.append((1, 0))
while len(q):
    node, d = q.popleft()
    parent.add(node)
    for nxt in G[node]:
        if nxt in parent:
            continue
        if nxt not in seen:
            q.append((nxt, d + 1))
            seen[nxt] = d + 1
        if seen[nxt] == d + 1:
            count[nxt] += count[node]
            count[nxt] %= MOD
print(count[N])

"""
幅探索でがちゃがちゃ
AC

解説
実装のシンプルさ以上に
que=[]
for v in que:
の実装が賢い

"""
