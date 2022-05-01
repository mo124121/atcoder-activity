H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
ret = []
# 最初のイチゴ検出
line = []
count = 1
for i, s in enumerate(S):
    if "#" in s:
        flag = False
        for c in s:
            if c == "#":
                if flag:
                    count += 1
                else:
                    flag = True
            line.append(count)
        ret.append(line)
        break
    else:
        ret.append(line)
# それ以降
for j, s in enumerate(S):
    if j <= i:
        continue
    if "#" in s:
        line = []
        count += 1
        flag = False
        for c in s:
            if c == "#":
                if flag:
                    count += 1
                else:
                    flag = True
            line.append(count)
    ret.append(line)

for r in ret:
    print(*r)

"""
単純に横方向に走査していって、次のが現れるまで同じのわりあててたら良くない？
何もないケースへの対処を考えるべき
上の行に出てたらコピーしてきたらいい、上の行になかったらどうする？
逆にlistの参照をうまく使うほうがいいのかもしれない、形は決まんないけど下とおんなじです！みたいな

AC
解説後
回答の空間が広いっぽいからか、種類が多い
再帰で分けるのはピンとこない
右方向に埋め→左方向に埋め、上方向に埋め、下方向に埋めはわかりやすい


"""
