from collections import deque


N, Q = map(int, input().split())
nxt = [0] * (N + 1)
pre = [0] * (N + 1)

ret = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, y = query
        nxt[x] = y
        pre[y] = x
    elif query[0] == 2:
        _, x, y = query
        nxt[x] = 0
        pre[y] = 0
    else:
        x = query[1]
        y = pre[x]
        r = deque()

        while x != 0:
            r.append(x)
            x = nxt[x]
        while y != 0:
            r.appendleft(y)
            y = pre[y]
        ret.append(list(r))

for r in ret:
    print(len(r), *r)
