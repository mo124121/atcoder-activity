from bisect import bisect, bisect_left


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
seen_b = set()
b_sizes = []
for b in B:
    seen_b.add(b)
    b_sizes.append(len(seen_b))

ok = dict()
seen_a = set()
seen_b = set()
a_not_b = set()
b_not_a = set()
skip_count = 0
for i_a, a in enumerate(A):
    seen_a.add(a)
    if a not in seen_b:
        a_not_b.add(a)
    a_size = len(seen_a)
    b_i = bisect_left(b_sizes, a_size)
    b_j = bisect(b_sizes, a_size)
    if b_i < N:
        b = B[b_i]
        seen_b.add(b)
        if b not in seen_a:
            b_not_a.add(b)

    if skip_count > 0:
        skip_count -= 1
        continue

    del_set = set()
    for a_k in a_not_b:
        if a_k in seen_b:
            del_set.add(a_k)
    a_not_b.difference_update(del_set)

    del_set = set()
    for b_k in b_not_a:
        if b_k in seen_a:
            del_set.add(b_k)
    b_not_a.difference_update(del_set)

    if len(a_not_b) == 0 and len(b_not_a) == 0:
        ok[i_a + 1] = (b_i + 1, b_j + 1)
    else:
        skip_count = len(a_not_b) - 1


Q = int(input())
ret = []
for i in range(Q):
    x, y = map(int, input().split())
    if x not in ok:
        ret.append("No")
        continue
    l, r = ok[x]
    if l <= y < r:
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

"""
