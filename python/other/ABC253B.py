H, W = map(int, input().split())
S = [input() for _ in range(H)]

count = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "o":
            if count == 0:
                h1, w1 = h, w
                count += 1
            else:
                print(abs(h1 - h) + abs(w1 - w))
                exit()
