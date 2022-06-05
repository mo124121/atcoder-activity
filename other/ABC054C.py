import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int, input().split())
from collections import defaultdict

G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


ret = 0
seen = set()


def dfs(node):
    if len(seen) == N - 1:
        return 1
    seen.add(node)
    ret = 0
    for nxt in G[node]:
        if nxt not in seen:
            ret += dfs(nxt)
    seen.discard(node)
    return ret


print(dfs(1))

"""
Nが小さい

木になるまで辺を減らした時に
全体にたどり着ける場合の全列挙
28C7 ちょっと大きい
もうちょっと枝切りしたい

普通にdfsしてみては？
"""
