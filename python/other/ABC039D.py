H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 収縮
S_pre = []
for h in range(H):
    line = []
    for w in range(W):
        flag = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                hn = h + i
                wn = w + j
                if 0 <= hn < H and 0 <= wn < W and S[hn][wn] == ".":
                    flag = False
                    break
        if flag:
            line.append("#")
        else:
            line.append(".")
    S_pre.append(line)

# 拡大
S_post = []
for h in range(H):
    line = []
    for w in range(W):
        flag = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                hn = h + i
                wn = w + j
                if 0 <= hn < H and 0 <= wn < W and S_pre[hn][wn] == "#":
                    flag = True
                    break
        if flag:
            line.append("#")
        else:
            line.append(".")
    S_post.append(line)


# 一致確認
for h in range(H):
    for w in range(W):
        if S[h][w] != S_post[h][w]:
            print("impossible")
            exit()
print("possible")
for line in S_pre:
    print(*line, sep="")

"""
1回縮小して膨張させて一致すればokか？

"""
