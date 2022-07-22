import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N = int(input())
from collections import defaultdict

G = defaultdict(list)
E = [(0, 0)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    E.append((a, b))

depth = [-1] * (N + 1)


def dfs(node):
    for nxt in G[node]:
        if depth[nxt] < 0:
            depth[nxt] = depth[node] + 1
            dfs(nxt)


depth[1] = 0
dfs(1)

ret = [0] * (N + 1)
Q = int(input())
for i in range(Q):
    t, e, x = map(int, input().split())
    a, b = E[e]
    if t == 2:
        a, b = b, a
    if depth[a] > depth[b]:
        ret[a] += x
    else:
        ret[b] -= x
        ret[1] += x


def solve(node):
    for nxt in G[node]:
        if depth[node] < depth[nxt]:
            ret[nxt] += ret[node]
            solve(nxt)


solve(1)
print(*ret[1:], sep="\n")

"""
木累積和、みたいな、imosのほうが正しい？
aが子ならそのノードに足しておく
aが親ならルートに足す＆bから引く

"""
