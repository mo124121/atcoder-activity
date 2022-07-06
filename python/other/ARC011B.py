N = int(input())
W = input().lower()

import re

W = re.sub(r"[aeiouy\.\,]", r"", W)
repl = [
    r"[zr]",
    r"[bc]",
    r"[dw]",
    r"[tj]",
    r"[fq]",
    r"[lv]",
    r"[sx]",
    r"[pm]",
    r"[hk]",
    r"[ng]",
]
for i, pat in enumerate(repl):
    W = re.sub(pat, str(i), W)
ret = W.split()
print(*ret)

"""
pythonならstrとかreを使えば楽勝ですよ
30000文字

AC
解説後
str.maketransとかいうの超便利
"""
