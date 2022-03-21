from functools import lru_cache
import sys

sys.setrecursionlimit(10**6)

N, X = map(int, input().split())

size = [0] * (N + 1)
putty = [0] * (N + 1)
size[0] = 1
putty[0] = 1

for i in range(N):
    size[i + 1] = 2 * size[i] + 3
    putty[i + 1] = 2 * putty[i] + 1


@lru_cache(maxsize=None)
def burger(l, x):
    if l == 0:
        return 1
    if x <= 1:
        return 0

    if size[l - 1] + 2 > x:
        return burger(l - 1, x - 1)
    elif size[l - 1] + 2 == x:
        return putty[l - 1] + 1
    elif size[l - 1] + 2 < x:
        return putty[l - 1] + 1 + burger(l - 1, x - size[l - 1] - 2)
    else:
        return putty[l]


p = burger(N, X)

print(p)
