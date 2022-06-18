from collections import Counter


N = int(input())
A = list(map(int, input().split()))

count = Counter()
count[A[0]] += 1
ret = 0
for i, a in enumerate(A[1:]):
    ret += i + 1 - count[a]
    count[a] += 1

print(ret)
