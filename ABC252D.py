from collections import Counter


N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
M = len(count)
B = list(count.values())
s = sum(B)
left = 0
right = s - B[0]
ret = 0
for i in range(1, M - 1):
    left += B[i - 1]
    right -= B[i]
    ret += left * B[i] * right

print(ret)
