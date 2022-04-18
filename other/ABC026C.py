from collections import defaultdict


N = int(input())
G = defaultdict(list)

for i in range(2, N + 1):
    boss = int(input())
    G[boss].append(i)


def rec(i):
    min_s = 10**17
    max_s = 0
    for child in G[i]:
        s = rec(child)
        min_s = min(min_s, s)
        max_s = max(max_s, s)
    if max_s == 0:
        return 1
    else:
        return min_s + max_s + 1


print(rec(1))

"""
グラフっぽい
N<20なので動けばいい
木構造
"""
