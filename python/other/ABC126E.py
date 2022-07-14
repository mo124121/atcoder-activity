import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int, input().split())
from collections import defaultdict

G = defaultdict(list)
for i in range(M):
    a, b, _ = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


depth = [-1] * (N + 1)


def dfs(node):
    for nxt in G[node]:
        if depth[nxt] < 0:
            depth[nxt] = depth[node] + 1
            dfs(nxt)


ret = 0
for i in range(1, N + 1):
    if depth[i] < 0:
        ret += 1
        dfs(i)

print(ret)
