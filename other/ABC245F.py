from collections import defaultdict

import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


def main():
    N, M = map(int, input().split())

    G = defaultdict(list)
    Grev = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    TRUE = 1
    FALSE = 0
    UNSET = -1
    loop_flags = {}

    def rec(node):
        if node in loop_flags:
            if loop_flags[node] != FALSE:
                loop_flags[node] = TRUE
                return loop_flags[node]
        loop_flags[node] = UNSET
        for nxt in G[node]:
            flag = rec(nxt)
            if flag == TRUE:
                loop_flags[node] = TRUE
                return TRUE

        loop_flags[node] = FALSE
        return FALSE

    ans = 0

    for i in range(1, N + 1):
        if i not in G:
            loop_flags[i] = FALSE

    for i in range(1, N + 1):
        if rec(i) == TRUE:
            ans += 1

    print(ans)


main()
