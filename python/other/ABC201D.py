H, W = map(int, input().split())
A = [input() for _ in range(H)]
Tscore = [[0] * W for _ in range(H)]
for h in reversed(range(H)):
    for w in reversed(range(W)):
        choices = []
        if h + 1 == H and w + 1 == W:
            choices.append(0)
        if h + 1 < H:
            choices.append(Tscore[h + 1][w])
        if w + 1 < W:
            choices.append(Tscore[h][w + 1])

        if (h + w) % 2:
            Tscore[h][w] = (-1) ** int(A[h][w] == "-") + min(choices)
        else:
            Tscore[h][w] = (-1) ** int(A[h][w] == "+") + max(choices)

Tscore[0][0] -= (-1) ** int(A[0][0] == "+")

if Tscore[0][0] == 0:
    print("Draw")
elif Tscore[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")
