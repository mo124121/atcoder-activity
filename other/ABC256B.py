from collections import deque


N = int(input())
A = list(map(int, input().split()))
P = 0
stat = []
for a in A:
    for i in range(len(stat)):
        stat[i] += a
    stat.append(a)
for s in stat:
    if s >= 4:
        P += 1
print(P)
