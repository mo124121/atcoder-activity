from collections import deque


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
D = []
for i in range(R):
    D.append(list(input()))


q = deque()
q.append((sy - 1, sx - 1, 0))
mvs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
while len(q):
    y, x, c = q.popleft()
    if (y, x) == (gy - 1, gx - 1):
        print(c)
        exit()
    for mv in mvs:
        ny = y + mv[0]
        nx = x + mv[1]
        if 0 <= ny < R and 0 <= nx < C and D[ny][nx] == ".":
            D[ny][nx] = c + 1
            q.append((ny, nx, c + 1))
