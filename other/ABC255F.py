import sys

sys.setrecursionlimit(10**6)
if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


N = int(input())
P = list(map(int, input().split()))
I = list(map(int, input().split()))

I_rev = {I[i]: i for i in range(N)}

ret = [[0] * 2 for _ in range(N + 1)]


def rec(lp, li, n):
    if n == 0:
        return 0
    root = P[lp]
    i = I_rev[root]

    if i < li or i >= li + n:
        return -1

    l_size = i - li
    r_size = n - 1 - l_size
    ret[root][0] = rec(lp + 1, li, l_size)
    ret[root][1] = rec(lp + 1 + l_size, li + l_size + 1, r_size)
    if ret[root][0] == -1:
        return -1
    if ret[root][1] == -1:
        return -1
    return root


if P[0] != 1 or -1 == rec(0, 0, N):
    print(-1)
else:
    for i in range(1, N + 1):
        print(*ret[i])


"""
サンプル例を題材に、子の木がどういう関係になるか眺めるのが重要そう

"""
