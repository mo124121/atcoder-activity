H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
MOD = 10**9 + 7

hor = [[0] * W for _ in range(H)]
ver = [[0] * W for _ in range(H)]
dia = [[0] * W for _ in range(H)]
pat = [[0] * W for _ in range(H)]
pat[0][0] = 1

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        if 0 < w:
            hor[h][w] = (hor[h][w - 1] + pat[h][w - 1]) % MOD
        if 0 < h:
            ver[h][w] = (ver[h - 1][w] + pat[h - 1][w]) % MOD
        if 0 < h and 0 < w:
            dia[h][w] = (dia[h - 1][w - 1] + pat[h - 1][w - 1]) % MOD
        pat[h][w] += (hor[h][w] + dia[h][w] + ver[h][w]) % MOD

print(pat[H - 1][W - 1])

"""
BFSしつつ、どう数え上げるか？縦横のみ
fenwickを使って効率化する？　縦と横はまだしも斜めがだるい
累積和的でいいはず、2つ前までの累積和＋前のマス（縦横入る可能性があるので

だるくなって解説見る
方針はあってる
dfsじゃなくていい,dpでよりシンプルになる

"""
