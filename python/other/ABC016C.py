from collections import defaultdict


N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
ret = [0] * (N + 1)

fr_fr_set = set()
for i in range(1, N + 1):
    fr_fr_set.clear()
    for fr in G[i]:
        for fr_fr in G[fr]:
            fr_fr_set.add(fr_fr)
    for fr in G[i]:
        fr_fr_set.discard(fr)
    fr_fr_set.discard(i)
    ret[i] = len(fr_fr_set)


print(*ret[1:], sep="\n")

"""
グラフ的にカウント
"""
