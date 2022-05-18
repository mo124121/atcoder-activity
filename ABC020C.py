from heapq import heappop, heappush


H, W, T = map(int, input().split())
S = [input() for _ in range(H)]

# スタートとゴールを探す
for h in range(H):
    for w in range(W):
        if S[h][w] == "S":
            start = (h, w)
        elif S[h][w] == "G":
            goal = (h, w)

# あるxによる最短時間を探す
def search(x):
    heap = []
    mvs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    heappush(heap, (0, start))
    seen = {}
    while len(heap):
        t, (h, w) = heappop(heap)
        if S[h][w] == "G":
            return t
        if (h, w) in seen:
            continue
        seen[(h, w)] = t
        for mv in mvs:
            nh = h + mv[0]
            nw = w + mv[1]
            nt = t + 1
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue

            if S[nh][nw] == "#":
                nt += x - 1
            if (nh, nw) not in seen:
                heappush(heap, (nt, (nh, nw)))


# 2分探索でT以内にたどり着けるxを探す

l = 0
r = 10**9 + 1
while r - l > 1:
    m = (r + l) // 2
    if search(m) <= T:
        l = m
    else:
        r = m
print(l)


"""
2分探索とダイクストラでは？
H,W<10
ワーシャルフロイドっぽくない
"""
