from collections import Counter
from itertools import permutations


N, C = map(int, input().split())

D = [list(map(int, input().split())) for _ in range(C)]
c = [list(map(int, input().split())) for _ in range(N)]

count = [Counter() for _ in range(3)]

for i in range(N):
    for j in range(N):
        count[(i + j) % 3][c[i][j]] += 1

INF = 10**18
ret = INF
for pat in permutations(range(C), 3):
    r = 0
    for i in range(3):
        for k, v in count[i].items():
            r += v * D[k - 1][pat[i]]
    ret = min(ret, r)
print(ret)
