from collections import deque


Q = int(input())

q = deque()

ret = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, c = query
        q.append((x, c))
    else:
        c = query[1]
        r = 0
        while c > 0:
            x, ci = q.popleft()
            if c < ci:
                r += x * c
                q.appendleft((x, ci - c))
                c = 0
            else:
                r += x * ci
                c -= ci
        ret.append(r)

print(*ret, sep="\n")
