from collections import defaultdict, deque
from heapq import heappop, heappush


N, M, X, Y = map(int, input().split())

G = defaultdict(list)
for i in range(M):
    a, b, t, k = map(int, input().split())
    G[a].append((b, t, k))
    G[b].append((a, t, k))

q = deque()
t = 0
h = []
heappush(h, (t, X))
seen = set()

while len(h):
    ti, node = heappop(h)
    if node in seen:
        continue
    seen.add(node)
    if node == Y:
        print(ti)
        exit()
    for nxt, t, k in G[node]:
        if nxt not in seen:
            tn = ti + t
            if ti % k != 0:
                tn += k - ti % k
            heappush(h, (tn, nxt))


print(-1)


"""
ちょっとややこしいけど、普通に幅探索問題に見える
heapを使ったほうがよさそうか
TLE 無限ループがあるみたい
"""
