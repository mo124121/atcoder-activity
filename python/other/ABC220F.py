import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


from collections import Counter, defaultdict

N = int(input())
G = defaultdict(list)

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


depth = defaultdict(lambda x: -1)
depth[1] = 0
child_size = Counter()


def calc_dissum(node):
    ret = 0
    for nxt in G[node]:
        if nxt not in depth:
            depth[nxt] = 1 + depth[node]
            ret += depth[nxt]
            ret += calc_dissum(nxt)
            child_size[node] += child_size[nxt]
    child_size[node] += 1
    return ret


ans = [0] * (N + 1)
ans[1] = calc_dissum(1)


def rec(node, par=-1):
    for nxt in G[node]:
        if nxt != par:
            ans[nxt] = ans[node] + N - 2 * child_size[nxt]
            rec(nxt, par=node)


rec(1)

print(*ans[1:], sep="\n")

"""
解説AC


"""
