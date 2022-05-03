from collections import deque


H, W = map(int, input().split())
S = [["#"] * (W + 2)]
S += [["#"] + list(input()) + ["#"] for _ in range(H)]
S += [["#"] * (W + 2)]


# 最短経路
q = deque()
q.append((1, 1, 0))
S[1][1] = "1"
mvs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
while len(q):
    h, w, c = q.popleft()
    if h == H and w == W:
        break

    for mv in mvs:
        nh, nw = h + mv[0], w + mv[1]
        if S[nh][nw] == ".":
            q.append((nh, nw, c + 1))
            S[nh][nw] = str(c + 1)
if (h, w) != (H, W):
    print(-1)
    exit()


# 黒をカウント
b = 0
for h in range(1, H + 1):
    for w in range(1, W + 1):
        if S[h][w] == "#":
            b += 1

print(H * W - b - c - 1)

"""
最短経路を探索→経由マスを特定→経由しないマスの色を変える
"""
