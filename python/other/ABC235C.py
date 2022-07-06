N, Q = map(int, input().split())
a = list(map(int, input().split()))
from collections import defaultdict

a_count = defaultdict(int)
a_number_count = {}

for i in range(N):
    a_count[a[i]] += 1
    a_number_count[(a[i], a_count[a[i]])] = i + 1

ret = []
for i in range(Q):
    x, k = map(int, input().split())
    if (x, k) in a_number_count:
        ret.append(a_number_count[(x, k)])
    else:
        ret.append(-1)

print(*ret, sep="\n")
