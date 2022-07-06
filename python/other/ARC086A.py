from collections import defaultdict
from email.policy import default


N, K = map(int, input().split())
A = list(map(int, input().split()))

count = defaultdict(int)
for a in A:
    count[a] += 1

vs = list(count.values())
vs.sort()
ret = sum(vs[:-K])

print(ret)
