import re

S = input()
r = re.search(r"(.).{0,1}\1", S)
if r:
    s = r.span()
    print(s[0] + 1, s[1])
else:
    print(-1, -1)

"""
まず連続してたらNG
連続してなかったら…OK?
aba <-ngのはず
2文字空いたら大丈夫？

2文字連続or1文字空きのがあればNG　それ以外はOK?

"""
