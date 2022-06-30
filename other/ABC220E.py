from functools import lru_cache
import sys

sys.setrecursionlimit(10**6 + 2)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N, D = map(int, input().split())
MOD = 998244353


@lru_cache(maxsize=None)
def root_path(n, d):
    if n == 0:
        return 0
    l = n
    r = d - l
    ret = 0
    if 0 <= r:
        ret += pow(2, max(0, l - 1), MOD) * pow(2, max(r - 1, 0), MOD) % MOD
        if l != r:
            ret = ret * 2 % MOD
    ret += root_path(n - 1, d)
    return ret


def rec(n, d):
    if n == 1:
        return 0
    ret = (rec(n - 1, d) * 2 + root_path(n, d)) % MOD
    return ret


print(rec(N, D) * 2 % MOD)
