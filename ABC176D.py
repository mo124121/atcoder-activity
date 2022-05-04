from heapq import heappop, heappush


H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

S = [list(input()) for _ in range(H)]
INF = 10**6
cost = [[INF] * W for _ in range(H)]
cost[Ch][Cw] = 0
he = [(0, Ch, Cw)]

mvs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while len(he):
    while len(he):
        c, h, w = heappop(he)
        if (h, w) == (Dh, Dw):
            print(c)
            exit()
        # 徒歩
        for mv in mvs:
            nh = h + mv[0]
            nw = w + mv[1]
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] != "#" and cost[nh][nw] > c:
                    heappush(he, (c, nh, nw))
                    cost[nh][nw] = c
    # ワープ元登録
    for nh in range(H):
        for nw in range(W):
            if cost[nh][nw] == c:
                heappush(he, (c, nh, nw))
    c_prev = c
    # ワープ
    while len(he):
        c, h, w = heappop(he)
        if c == c_prev + 1:
            heappush(he, (c, h, w))
        c += 1
        for x in range(-2, 3):
            for y in range(-2, 3):
                if abs(x) + abs(y) < 2:
                    continue
                nh = h + y
                nw = w + x
                if 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] != "#" and cost[nh][nw] > c:
                        heappush(he, (c, nh, nw))
                        cost[nh][nw] = c

print(-1)
"""
幅探索亜種

H,W<10**3
HW<10**6
遷移探索範囲 25

ワープ数をheapで管理しておくのが良さそう


"""
