import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


seen = set()


Q = int(input())
ret = []
for i in range(Q):
    seen.clear()
    x, k = map(int, input().split())
    q = deque()
    q.append((x, k))
    while q:
        xi, ki = q.popleft()
        seen.add(xi)
        if ki > 0:
            for nxt in G[xi]:
                if nxt not in seen:
                    q.append((nxt, ki - 1))
    r = sum(seen)
    ret.append(r)

print(*ret, sep="\n")
