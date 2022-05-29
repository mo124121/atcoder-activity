H, W = map(int, input().split())
S = [input() for _ in range(H)]

ret = 0
for h in range(H - 1):
    for w in range(W - 1):
        count = 0
        for hn in [h, h + 1]:
            for wn in [w, w + 1]:
                if S[hn][wn] == "#":
                    count += 1
        if count % 2 == 1:
            ret += 1
print(ret)
