from collections import deque


H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

q = deque()

# 黒ます追加
for h in range(H):
    for w in range(W):
        if A[h][w] == "#":
            q.append((0, h, w))

# 白ます埋め
mvs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while len(q):
    c, h, w = q.popleft()
    for mv in mvs:
        nh = h + mv[0]
        nw = w + mv[1]
        if 0 <= nh < H and 0 <= nw < W and A[nh][nw] == ".":
            A[nh][nw] = "#"
            q.append((c + 1, nh, nw))
print(c)


"""
黒マスから最短でどれくらい離れているか問題
H,W<1000
よくあるサイズ

幅探索していったらいい
"""
