H, W, N, M = map(int, input().split())

A = [0] * N
B = [0] * N
wall = [[False] * (W + 1) for i in range(H + 1)]

for i in range(N):
    A[i], B[i] = map(int, input().split())
for i in range(M):
    c, d = map(int, input().split())
    wall[c][d] = True

l_w = [[False] * (W + 1) for _ in range(H + 1)]
for i in range(N):
    a, b = A[i], B[i]
    if l_w[a][b]:
        continue
    for w in range(b, W + 1):
        if wall[a][w]:
            break
        l_w[a][w] = True
    for w in range(b - 1, 0, -1):
        if wall[a][w]:
            break
        l_w[a][w] = True
l_h = [[False] * (W + 1) for _ in range(H + 1)]
for i in range(N):
    a, b = A[i], B[i]
    if l_h[a][b]:
        continue
    for h in range(a, H + 1):
        if wall[h][b]:
            break
        l_h[h][b] = True
    for h in range(a - 1, 0, -1):
        if wall[h][b]:
            break
        l_h[h][b] = True
ret = 0
for w in range(1, W + 1):
    for h in range(1, H + 1):
        if l_w[h][w] or l_h[h][w]:
            ret += 1

print(ret)


"""
なるほどわからん

X,Yを分解してufしていくとかいいかも
まずブロックを見て、一塊を作る
明かりをみて、塊を光ってるフラグのマスにつなげる
最後に全体操作して接続している場合はカウントする

解説後
縦横分けて愚直でいい、もう見たことあるやつを切ればHWの中で収まる


"""
