from functools import lru_cache
from math import ceil, floor

X = int(input())
MOD = 998244353


memo = {}


def rec(X):
    if X in memo:
        return memo[X]
    if X <= 4:
        memo[X] = X
        return X
    a = X // 2
    b = X // 2 + X % 2
    ret = rec(a) * rec(b) % MOD
    memo[X] = ret
    return ret


print(rec(X))
