S = input().replace("10", "T")

RSF = [
    set(["ST", "SJ", "SQ", "SK", "SA"]),
    set(["HT", "HJ", "HQ", "HK", "HA"]),
    set(["DT", "DJ", "DQ", "DK", "DA"]),
    set(["CT", "CJ", "CQ", "CK", "CA"]),
]


def check(seen):
    for i in range(len(RSF)):
        flag = True
        for card in RSF[i]:
            if card not in seen:
                flag = False
                break
        if flag:
            return i
    return -1


seen = set()
for i in range(0, len(S), 2):
    seen.add(S[i : i + 2])
    r = check(seen)
    if r != -1:
        break

get = set()
ret = []
for i in range(0, len(S), 2):
    card = S[i : i + 2]
    if card in RSF[r]:
        get.add(card)
    else:
        ret.append(card)
    if len(get) == 5:
        break

if len(ret) == 0:
    print(0)
else:
    ret = "".join(ret)
    print(ret.replace("T", "10"))

"""
BNFとか言われててんぱったけどまあ良し
まず関係するもの以外は即捨てる
問題は関係するものが来た時どうするか？

別にクエリ先読みができるので、
一番先にそろうものをターゲットに決定し、
それ以外のやつは捨てていくムーブにする

"""
