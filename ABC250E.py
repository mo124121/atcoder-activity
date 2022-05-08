from random import randint

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
R_map = {}
for v in set(A + B):
    R_map[v] = randint(0, 10**18)


def hs(A):
    seen = set()
    s = 0
    r = [0]
    for a in A:
        if a not in seen:
            seen.add(a)
            s ^= R_map[a]
        r.append(s)
    return r


Ah = hs(A)
Bh = hs(B)

ret = []
Q = int(input())
for i in range(Q):
    x, y = map(int, input().split())
    if Ah[x] == Bh[y]:
        ret.append("Yes")
    else:
        ret.append("No")
print(*ret, sep="\n")

"""
order set使ったら楽勝なんじゃね？

クエリ先読みして、結果をおいておく、的な？


値ベースでやるのはしんどいか？

片方をソートしておく

ハッシュ計算はぶつかるか？数字がでかいからしんどそう

愚直を考える
N対Nのマッチングをとる問題
少なくとも集合の大きさは同じである必要がある
集合の数を各時点で保存　bisect　一致するかを確認する
順に数字を増やしていけば、全部の集合差を考える必要はない
いったん書いてみる


17WA/34
悪くはないはず

zobrist hashとな


"""
