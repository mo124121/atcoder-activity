from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
"""
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")
"""

n, x = map(int, input().split())
h = [0] + list(map(int, input().split()))

G = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


def rec(x, parent=0):
    ret = 0
    for child in G[x]:
        if child == parent:
            continue
        r = rec(child, x)
        if r >= 0:
            ret += r + 2
    if ret == 0 and h[x] == 0:
        ret = -1
    return ret


print(max(0, rec(x)))


"""
考察
部分木のコスト=Σ部分木のコスト+1 if 部分木に宝石があれば

"""
