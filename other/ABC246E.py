from collections import deque

N = int(input())
INF = 9
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
S = [[1] * (N + 2) for _ in range(N + 2)]
D = [[INF] * (2 + N) for _ in range(N + 2)]
for i in range(N):
    s = input()
    for j in range(N):
        S[i + 1][j + 1] = int(s[j] == "#")


D[Ax][Ay] = 0
moves = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
dq = deque()
dq.append((Ax, Ay))


def show():
    for s in D:
        print(*s)


while len(dq) > 0:
    x, y = dq.popleft()
    d = D[x][y]
    if (x, y) == (Bx, By):
        print(d)
        exit()
    for mx, my in moves:
        xt, yt = x, y
        while True:
            xt += mx
            yt += my
            if S[xt][yt] or D[xt][yt] <= d:
                break
            if D[xt][yt] < INF:
                continue
            D[xt][yt] = d + 1
            dq.append((xt, yt))
print(-1)
