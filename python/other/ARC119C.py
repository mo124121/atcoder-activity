from collections import Counter
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))
B = [(-1) ** i * a for i, a in enumerate(A)]

C = list(accumulate(B))
count = Counter()
count[0] += 1
ret = 0
for c in C:
    ret += count[c]
    count[c] += 1
print(ret)


"""
解説見る
まず判定条件が思いつかない

偶奇の発想は検討すべき


数式の変形は結構ありそう、これはやるべきだった
倍数の性質 11の倍数は偶数桁目・奇数桁目の差が11の倍数
今回に使うのはやや飛躍がある
"""
