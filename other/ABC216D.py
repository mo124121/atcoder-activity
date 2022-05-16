from collections import deque


N, M = map(int, input().split())
syls = []
for i in range(M):
    k = int(input())
    syls.append(list(map(int, input().split())))

surfaces = {}
erased = 0
q = []

for m in range(M):
    q.append((m, syls[m].pop()))

for m, v in q:
    if v in surfaces:
        for nxt in [surfaces[v], m]:
            if len(syls[nxt]):
                q.append((nxt, syls[nxt].pop()))
        erased += 1
    else:
        surfaces[v] = m

if erased == N:
    print("Yes")
else:
    print("No")
