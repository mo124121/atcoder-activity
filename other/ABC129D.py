H, W = map(int, input().split())
S = [input() for _ in range(H)]
count = [[0] * W for _ in range(H)]

# 縦方向
for w in range(W):
    l = -1
    r = 0
    while r < H:
        if S[r][w] == "#":
            for i in range(l + 1, r):
                count[i][w] = r - l - 1
            l = r
        r += 1
    for i in range(l + 1, r):
        count[i][w] = r - l - 1

# 横方向しつつ最大値探索
ret = 0
for h in range(H):
    l = -1
    r = 0
    while r < W:
        if S[h][r] == "#":
            for i in range(l + 1, r):
                count[h][i] += r - l - 2 + (count[h][i] == 0)
                ret = max(ret, count[h][i])
            l = r
        r += 1
    for i in range(l + 1, r):
        count[h][i] += r - l - 2 + (count[h][i] == 0)
        ret = max(ret, count[h][i])
print(ret)


"""
超どっかで見たことある

HとWを分割する、それぞれに対してまっすぐ方向に照らせる数をカウントして格納する
たぶん尺取りでいい

"""
