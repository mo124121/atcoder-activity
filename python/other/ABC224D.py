M = int(input())
from collections import defaultdict, deque

G = defaultdict(list)
for i in range(M):
    a, b = input().split()
    G[a].append(b)
    G[b].append(a)

p = input().replace(" ", "")
goal = "12345678"

seen = set()

q = deque()
q.append((0, p))
seen.add(p)

ALL = set("123456789")
while q:
    count, p = q.popleft()
    if p == goal:
        print(count)
        exit()
    seen.add(p)
    s = ALL.difference(set(p)).pop()
    for nxt in G[s]:
        pn = list(p)
        pn[pn.index(nxt)] = s
        pn = "".join(pn)
        if pn not in seen:  # <-ここ
            q.append((count + 1, pn))
            seen.add(pn)


print(-1)

"""
幅探索

時間足りない幅探索は枝切りを2回するイメージ
遷移前と遷移後

遷移する直前に確認するのがスマートそう
"""
