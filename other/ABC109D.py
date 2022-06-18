H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]


ret = []
for h in range(H):
    for w in range(W - 1):
        if a[h][w] % 2 == 1:
            ret.append((h + 1, w + 1, h + 1, w + 2))
            a[h][w] -= 1
            a[h][w + 1] += 1

for h in range(H - 1):
    if a[h][W - 1] % 2 == 1:
        ret.append((h + 1, W, h + 2, W))
        a[h][W - 1] -= 1
        a[h + 1][W - 1] += 1

print(len(ret))
for r in ret:
    print(*r)
