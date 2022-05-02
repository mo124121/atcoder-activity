from collections import Counter, defaultdict


N = int(input())
count = defaultdict(int)
S = []
for i in range(N):
    S.append(input())
count = Counter(S)
m = 0
for v in count.values():
    m = max(m, v)
ret = []
for k, v in count.items():
    if v == m:
        ret.append(k)
ret.sort()
print(*ret, sep="\n")
