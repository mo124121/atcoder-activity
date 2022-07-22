from collections import Counter, defaultdict


N = int(input())
A = list(map(int, input().split()))
count = Counter()
ret = 0
for i, a in enumerate(A):
    ret += count[-a + i]
    count[a + i] += 1


print(ret)
