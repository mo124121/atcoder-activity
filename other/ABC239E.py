from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(500 * 500)  # 追加

N, Q = map(int, input().split())
X = [0] + list(map(int, input().split()))

G = defaultdict(list)
for i in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

G_list = defaultdict(list)
seen = {}


def rec(i):
    if i in seen:
        return []
    seen[i] = True
    if i != 1 and len(G[i]) == 1:
        G_list[i] = [X[i]]
        return G_list[i]

    h = [X[i]]
    for child in G[i]:
        h += rec(child).copy()
    h.sort()
    G_list[i] = h[-20:]
    return G_list[i]


rec(1)

ret = [0] * Q

for i in range(Q):
    V, K = map(int, input().split())
    ret[i] = G_list[V][len(G_list[V]) - K]

print(*ret, sep="\n")
