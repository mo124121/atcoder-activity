from collections import deque


H, W = map(int, input().split())
C = [list(input()) + ["#"] for _ in range(H)]
C = C + [["#"] * (W + 2)]

q = deque()
q.append((0, 0, 1))
ret = 1

while len(q):
    h, w, step = q.pop()
    if C[h][w] == ".":
        C[h][w] = "#"
        ret = max(ret, step)
        q.append((h + 1, w, step + 1))
        q.append((h, w + 1, step + 1))

print(ret)
