N, M = map(int, input().split())
from collections import defaultdict
from itertools import permutations

G = defaultdict(list)
edges = set()
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    edges.add((a, b))
    edges.add((b, a))

ret = 0
for pat in permutations(range(2, N + 1)):
    pat = [1] + list(pat)
    flag = True
    for i in range(N - 1):
        if (pat[i], pat[i + 1]) not in edges:
            flag = False
            break
    if flag:
        ret += 1


print(ret)

"""
Nが小さい

木になるまで辺を減らした時に
全体にたどり着ける場合の全列挙
28C7 ちょっと大きい
もうちょっと枝切りしたい

普通にdfsしてみては？

解説後
DFSで良かった
辺を見ずにnodeの順列で辺が存在するかでもよい
"""
