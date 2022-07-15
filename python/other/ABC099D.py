from collections import Counter
from itertools import permutations


N, C = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

count = [Counter() for _ in range(3)]
cost = [[0] * 3 for _ in range(C)]

for i in range(N):
    for j in range(N):
        for k in range(C):
            cost[k][(i + j) % 3] += D[c[i][j] - 1][k]

INF = 10**18
ret = INF
for pat in permutations(range(C), 3):
    r = 0
    for i in range(3):
        r += cost[pat[i]][i]
    ret = min(ret, r)
print(ret)


"""
事前に切り替え
逆に遅くなってる…
"""
