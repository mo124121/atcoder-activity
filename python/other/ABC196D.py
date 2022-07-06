from itertools import combinations


H, W, A, B = map(int, input().split())

vert = (H - 1) * W
hori = H * (W - 1)

ret = 0
for pat in combinations(range(vert + hori), A):
    locked = [[False] * W for _ in range(H)]
    invalid = False
    for p in pat:
        if p < vert:
            h = p // W
            w = p % W
            if locked[h][w] or locked[h + 1][w]:
                invalid = True
            locked[h][w] = True
            locked[h + 1][w] = True
        else:
            p -= vert
            h = p // (W - 1)
            w = p % (W - 1)
            if locked[h][w] or locked[h][w + 1]:
                invalid = True
            locked[h][w] = True
            locked[h][w + 1] = True
    if not invalid:
        ret += 1
print(ret)
