N = int(input())

from collections import defaultdict

G = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


path = []


def rec(node, par):
    pass


if rec == 1:
    print("Fennec")
else:
    print("Snuke")
"""
道がN-1 木

お互い近づけ合うようにぬっていって、
塗られていない部分木の大きさを数える感じ

"""
