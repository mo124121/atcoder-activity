from collections import Counter

N, T = map(int, input().split())
A = list(map(int, input().split()))


count = Counter()
v_min = 10**18
for a in A:
    count[a - v_min] += 1
    v_min = min(v_min, a)

print(count[max(count.keys())])

"""
解説見た
相異なるという条件を見落としててクッソ難しく考えていた
"""
