from bisect import bisect_left

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

Qrev = [0] * (N + 1)
for i, q in enumerate(Q):
    Qrev[q] = i + 1


INF = 10**6
dp = [INF] * (N + 2)
dp[0] = 0
dp2 = []
for p in P:
    p2 = p
    dp2.clear()
    while p2 <= N:
        i = Qrev[p2]
        j = bisect_left(dp, i)
        dp2.append((j, i))
        p2 += p
    for j, i in dp2:
        dp[j] = min(dp[j], i)

for i, v in enumerate(dp):
    if v == INF:
        break
print(i - 1)
