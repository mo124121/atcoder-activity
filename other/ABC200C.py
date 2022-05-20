from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

seen = defaultdict(int)
for a in A:
    seen[a % 200] += 1

ret = 0
for v in seen.values():
    ret += v * (v - 1) // 2
print(ret)
