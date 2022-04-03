from collections import deque

N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
INF = N * N
WALL = -1
NOT_PASSED = INF
S = [[WALL] * (N + 2) for _ in range(N + 2)]


def show():
    for s in S:
        print(*s)


for i in range(N):
    s = input()
    for j in range(N):
        if s[j] == "#":
            S[i + 1][j + 1] = WALL
        else:
            S[i + 1][j + 1] = INF

mvs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

S[ax][ay] = 0
Q = deque([(ax, ay)])

while len(Q):
    x, y = Q.popleft()
    c = S[x][y]
    if (x, y) == (bx, by):
        print(c)
        exit()
    for mx, my in mvs:
        nx, ny = x, y
        while True:
            nx += mx
            ny += my
            if S[nx][ny] == WALL or S[nx][ny] <= c:
                break
            if S[nx][ny] != NOT_PASSED:
                continue
            S[nx][ny] = c + 1
            Q.append((nx, ny))
    # show()

print(-1)
