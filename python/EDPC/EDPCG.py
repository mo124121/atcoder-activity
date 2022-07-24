import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


from collections import defaultdict


N, M = map(int, input().split())

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)

memo = [-1] * (N)


def dfs(node, par=-1):
    if memo[node] > 0:
        return memo[node]
    ret = 0
    for nxt in G[node]:
        if nxt != par:
            ret = max(ret, dfs(nxt, node) + 1)
    memo[node] = ret
    return ret


ans = 0

for i in range(N):
    ans = max(ans, dfs(i, -1))

print(ans)
