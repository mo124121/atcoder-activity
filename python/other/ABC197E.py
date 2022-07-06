from collections import Counter, defaultdict


N = int(input())
CX = defaultdict(list)
for _ in range(N):
    x, c = map(int, input().split())
    CX[c].append(x)

INF = 10**18
pos = {0: 0}
for i in range(1, N + 1):
    if i not in CX:
        continue
    nxt = defaultdict(lambda: INF)
    xmax = max(CX[i])
    xmin = min(CX[i])
    for x, t in pos.items():
        nxt[xmax] = min(nxt[xmax], t + abs(xmax - xmin) + abs(xmin - x))
        nxt[xmin] = min(nxt[xmin], t + abs(xmin - xmax) + abs(xmax - x))
    pos = nxt

ret = INF
for k, v in pos.items():
    ret = min(ret, abs(k) + v)

print(ret)
