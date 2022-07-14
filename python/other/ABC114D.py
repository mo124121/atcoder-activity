from collections import Counter
from itertools import combinations

N = int(input())
if N < 10:
    print(0)
    exit()
base = list(range(2, N + 1))
primes = list()
while base[0] ** 2 <= N:
    tmp = base[0]
    primes.append(tmp)
    base = [e for e in base if e % tmp != 0]
primes += base

p_count = Counter()

for i in range(1, N + 1):
    v = i
    for p in primes:
        while v % p == 0:
            v //= p
            p_count[p] += 1
p_count2 = [v for v in p_count.values() if v >= 2]

ret = 0

# 75
for k, v in p_count.items():
    if v >= 74:
        ret += 1

# 15*5
for k1, v1 in p_count.items():
    for k2, v2 in p_count.items():
        if k1 != k2 and v1 >= 14 and v2 >= 4:
            ret += 1
# 3*25
for k1, v1 in p_count.items():
    for k2, v2 in p_count.items():
        if k1 != k2 and v1 >= 2 and v2 >= 24:
            ret += 1

for pat in combinations(p_count2, 3):
    if pat[0] >= 4 and pat[1] >= 4 and pat[2] >= 2:
        ret += 1
    if pat[0] >= 4 and pat[2] >= 4 and pat[1] >= 2:
        ret += 1
    if pat[2] >= 4 and pat[1] >= 4 and pat[0] >= 2:
        ret += 1
print(ret)


"""
全列挙はできない

約数の個数
各素数の使用個数の場合分けの積

解説見る
方針はあってるっぽい
"""
