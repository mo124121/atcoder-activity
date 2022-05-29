H, W = map(int, input().split())


ret = 10**10
S = [0] * 3
# 縦
for w in range(1, W // 2 + 1):
    S[0] = H * w
    wr = W - w
    # 縦
    S[1] = H * (wr // 2)
    S[2] = H * W - S[0] - S[1]
    ret = min(max(S) - min(S), ret)
    # 横
    S[1] = (H // 2) * wr
    S[2] = H * W - S[0] - S[1]
    ret = min(max(S) - min(S), ret)

# 横
for h in range(1, H // 2 + 1):
    S[0] = h * W
    hr = H - h
    # 横
    S[1] = W * (hr // 2)
    S[2] = H * W - S[0] - S[1]
    ret = min(max(S) - min(S), ret)
    # 縦
    S[1] = (W // 2) * hr
    S[2] = H * W - S[0] - S[1]
    ret = min(max(S) - min(S), ret)

print(ret)


"""
全探索でいいように見える
1つの大きさを変えつつ、残りは縦と横に割る
"""
