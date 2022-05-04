from collections import deque


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

q = deque()
q.append((0, Ch, Cw))

while len(q):
    c, h, w = q.popleft()
    if (h, w) == (Dh, Dw):
        print(c)
        exit()
    if cost[h][w] != INF:
        continue
    cost[h][w] = c
    for x in range(-2, 3):
        for y in range(-2, 3):
            nh = h + y
            nw = w + x
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] != "#" and cost[nh][nw] == INF:
                    if abs(x) + abs(y) > 1:
                        q.append((c + 1, nh, nw))
                    else:
                        q.appendleft((c, nh, nw))


print(-1)

"""
幅探索亜種

H,W<10**3
HW<10**6
遷移探索範囲 25

ワープ数をheapで管理しておくのが良さそう

TLEだしちょっと戦略を変える



"""
