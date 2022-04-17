from bisect import bisect
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [0] * Q
R = [0] * Q
X = [0] * Q
for i in range(Q):
    L[i], R[i], X[i] = map(int, input().split())

seen = defaultdict(int)
pos_list = []
for i, a in enumerate(A):
    seen[a] += 1
    pos_list.append((a, i + 1, seen[a]))

pos_list.sort()
ret = []
for i in range(Q):

    l = bisect(pos_list, (X[i], L[i], 0))
    r = bisect(pos_list, (X[i], R[i], 10**6))

    r_x, r_i, r_c = pos_list[r - 1]
    if r_x != X[i]:
        r_c = 0
    if l != 0:
        l_x, l_i, l_c = pos_list[l - 1]
        if l_x == X[i]:
            r_c -= l_c
    ret.append(r_c)

print(*ret, sep="\n")
"""
考察
先読みして座標圧縮くさい

セグ木をうまく使いそうな気はするがいったんおいておく

N,Q<2*10**5
N**2は間に合わない、どうするか？

辞書でカウントにしても、各範囲毎にはおけない

クエリ先読みしてほしいのをリストアップしつつ、
LorRまでのXのカウントをストックする

少し落ち着こう



"""
