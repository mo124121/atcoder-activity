H, W = map(int, input().split())
S = [input() for _ in range(H)]
ret = 0

for h in range(H - 1):
    for w in range(W - 1):
        c = 0
        for x in [0, 1]:
            for y in [0, 1]:
                c += int(S[h + x][w + y] == "#")
        if c in [1, 3]:
            ret += 1

print(ret)
"""
めっちゃややこしく見えるが、
各マスで黒・白の辺の個数-1でいいのでは？
へこんでいる状況を考えると違う


解説後
問題文は理解できていたが、解法が思いつかず
解説賢い、マスではなく、格子の点を中心で考える
"""
