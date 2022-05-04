H, W = map(int, input().split())
S = [["."] * (W + 2)]
S += [["."] + list(input()) + ["."] for _ in range(H)]
S += [["."] * (W + 2)]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if S[h][w] == "#":
            continue
        c = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) == (0, 0):
                    continue
                if S[h + y][w + x] == "#":
                    c += 1
        S[h][w] = str(c)

for i in range(1, H + 1):
    print("".join(S[i][1:-1]))

