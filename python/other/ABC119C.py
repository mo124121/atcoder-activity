from itertools import product


N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
ret = 10**18
for pat in product(range(4), repeat=N):
    cost = [-10] * 4
    l = [0] * 4
    for i, p in enumerate(pat):
        cost[p] += 10
        l[p] += L[i]
    if -10 in cost[:3]:
        continue
    ret = min(ret, abs(A - l[0]) + abs(B - l[1]) + abs(C - l[2]) + sum(cost[:3]))
print(ret)
