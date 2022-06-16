from bisect import bisect, bisect_left
from collections import defaultdict


s = input()
t = input()

occurs = defaultdict(list)
for i, c in enumerate(s):
    occurs[c].append(i)

ret = 0
prev = -1
for c in t:
    if c not in occurs:
        print(-1)
        exit()
    i = bisect_left(occurs[c], prev + 1)
    if i == len(occurs[c]):
        ret += len(s)
        i = 0
    prev = occurs[c][i]

print(ret + prev + 1)


"""
リールの問題っぽい
tを左から見て行って、
s'上で出てくるやつを順々に追っていく形

毎回やると間に合わない
ある文字から次の文字が現れるindexのマップを事前に計算しておく
s+sでやるといいかな


sにない文字がtにあるとng

ある文字の次にあるアルファベットが来る最小のインデックス
あるアルファベットが来た時に今までで一番手前にあるアルファベット

方針を変える
sにおいて各アルファベットごとに出現する位置を記憶
現在位置以降で現れる場所に遷移していく


"""
