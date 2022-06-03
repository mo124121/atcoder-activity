from collections import Counter


N = int(input())
count = Counter()
for _ in range(N):
    S = input()
    count[S] += 1

ma = 0
for k, v in count.items():
    if ma < v:
        ret = k
        ma = v
print(ret)
