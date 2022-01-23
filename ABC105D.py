N, M = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict

count = defaultdict(int)
count[0] = 1
ret = 0
sum = 0

for i in range(N):
    sum += A[i]
    ret += count[sum % M]
    count[sum % M] += 1

print(ret)
