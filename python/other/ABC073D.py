from itertools import permutations
from scipy.sparse import *

N, M, R = map(int, input().split())
r = list(map(int, input().split()))

t = []
for i in range(M):
    a, b, c = map(int, input().split())
    t.append((a, b, c))

a, b, c = zip(*t)

l = csgraph.dijkstra(csr_matrix((c, (a, b)), [N + 1] * 2), 0)
print(min(sum(int(l[i][j]) for i, j in zip(a[:-1], a[1:])) for a in permutations(r)))
