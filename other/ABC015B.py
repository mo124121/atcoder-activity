N = int(input())
A = list(map(int, input().split()))

sum_bug = 0
sum_soft = 0
for a in A:
    if a != 0:
        sum_bug += a
        sum_soft += 1
print((sum_bug + sum_soft - 1) // sum_soft)
