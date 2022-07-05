from collections import deque


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

q = deque()

q.append((0, 0, 0))
S[0][0] = 0
mvs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
while q:
    c, h, w = q.popleft()
    for ha, wa in mvs:
        hn = h + ha
        wn = w + wa
        if 0 <= hn < H and 0 <= wn < W:
            if S[hn][wn] == ".":
                S[hn][wn] = c
                q.appendleft((c, hn, wn))

    for wa in range(-2, 3):
        for ha in range(-2, 3):
            if abs(wa) + abs(ha) == 4 or wa == ha == 0:
                continue
            hn = h + ha
            wn = w + wa
            if 0 <= hn < H and 0 <= wn < W:
                if S[hn][wn] == "#":
                    S[hn][wn] = c + 1
                    q.append((c + 1, hn, wn))

print(S[H - 1][W - 1])
