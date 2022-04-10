from collections import deque


Q = int(input())
dq = deque()
ret = []
for i in range(Q):

    S = input().split()
    if int(S[0]) == 1:
        dq.append((int(S[1]), int(S[2])))
    else:
        c = int(S[1])
        r = 0
        while True:
            y, d = dq.popleft()
            if c <= d:
                r += y * c
                dq.appendleft((y, d - c))
                break
            else:
                r += y * d
                c -= d
        ret.append(r)
for r in ret:
    print(r)
