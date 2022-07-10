import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N = int(input())
from collections import defaultdict

G = defaultdict(list)
for i in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))


depth = [-1] * (N + 1)
depth[1] = 0


def rec(node):
    for nxt, d in G[node]:
        if depth[nxt] == -1:
            depth[nxt] = depth[node] + d
            rec(nxt)


rec(1)

for i in range(1, N + 1):
    print(depth[i] % 2)
