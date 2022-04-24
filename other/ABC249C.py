from collections import defaultdict
from itertools import product


N, K = map(int, input().split())
S = [input() for _ in range(N)]
ret = 0
for pat in product((True, False), repeat=N):
    count = defaultdict(int)
    for i, s in enumerate(S):
        if pat[i]:
            continue
        for c in s:
            count[c] += 1
    r = 0
    for v in count.values():
        if v == K:
            r += 1
    ret = max(ret, r)
print(ret)
