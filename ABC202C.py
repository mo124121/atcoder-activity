from collections import Counter, defaultdict


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

count_C = Counter(C)
ret = 0

count_B = defaultdict(int)

for k, v in count_C.items():
    count_B[B[k - 1]] += v

for a in A:
    ret += count_B[a]
print(ret)
