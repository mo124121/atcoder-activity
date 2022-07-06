import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


N = int(input())
C = [0] + list(map(int, input().split()))

from collections import Counter, defaultdict

M = N - 1
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ret = []
seen = Counter()


def dfs(node, par=0):
    if seen[C[node]] == 0:
        ret.append(node)

    seen[C[node]] += 1

    for nxt in G[node]:
        if nxt != par:
            dfs(nxt, node)
    seen[C[node]] -= 1


dfs(1)

ret.sort()
print(*ret, sep="\n")
