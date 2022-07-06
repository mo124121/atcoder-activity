H, W = map(int, input().split())
S = [input() for _ in range(H)]
MOD = 998244353
flag_b = [False] * (H + W - 1)
flag_r = [False] * (H + W - 1)
for h in range(H):
    for w in range(W):
        if S[h][w] == "B":
            flag_b[h + w] = True
        elif S[h][w] == "R":
            flag_r[h + w] = True

ret = 1
for b, r in zip(flag_b, flag_r):
    if b and r:
        ret = 0
        break
    elif b or r:
        pass
    else:
        ret *= 2
        ret %= MOD


print(ret)
