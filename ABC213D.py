import sys

sys.setrecursionlimit(10**6)


N = int(input())
from collections import defaultdict

G = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    G[i].sort()

ret = []


def rec(node, par=0):
    ret.append(node)
    for nxt in G[node]:
        if nxt != par:
            rec(nxt, node)
            ret.append(node)


rec(1)

print(*ret)
