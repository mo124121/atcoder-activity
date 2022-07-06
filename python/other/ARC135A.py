from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")

X = int(input())

MOD = 998244353


@lru_cache(maxsize=None)
def rec(X):
    if X < 5:
        return X
    return (rec(X // 2) * rec((X + 1) // 2)) % MOD


print(rec(X))

"""
1 0 0 x
2 1 1 x
3 1 2 x
4 2 2 x
5 2 3 o

"""
