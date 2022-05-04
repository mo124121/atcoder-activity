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

q = [(0, Ch, Cw)]
q2 = []
mvs = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]

while len(q):
    while len(q):
        c, h, w = q.pop()
        q2.append((c, h, w))
        if (h, w) == (Dh, Dw):
            print(c)
            exit()
        if c > cost[h][w]:
            continue
        # 徒歩
        for mv in mvs:
            nh = h + mv[0]
            nw = w + mv[1]
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] != "#" and cost[nh][nw] == INF:
                    q.append((c, nh, nw))
                    cost[nh][nw] = c
    # ワープ
    while len(q2):
        c, h, w = q2.pop()
        c += 1
        for x in range(-2, 3):
            for y in range(-2, 3):
                nh = h + y
                nw = w + x
                if 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] != "#" and cost[nh][nw] == INF:
                        q.append((c, nh, nw))
                        cost[nh][nw] = c


print(-1)

"""
幅探索亜種

H,W<10**3
HW<10**6
遷移探索範囲 25

ワープ数をheapで管理しておくのが良さそう

TLEだしちょっと戦略を変える



"""
