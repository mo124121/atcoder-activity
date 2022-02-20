from collections import defaultdict
import sys

sys.setrecursionlimit(1000 ** 2)

N = int(input())

G = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

L = [0] * N
R = [0] * N

seen = {}
count = 0
INF = 10 ** 7


def rec(i):
    seen[i] = True
    if i != 0 and len(G[i]) == 1:
        global count
        count += 1
        L[i] = count
        R[i] = count
        return count, count
    L_i = INF
    R_i = 0
    for e in G[i]:
        if not e in seen:
            l, r = rec(e)
            L_i = min(L_i, l)
            R_i = max(R_i, r)
    L[i] = L_i
    R[i] = R_i
    return L_i, R_i


rec(0)

for i in range(N):
    print(L[i], R[i])
