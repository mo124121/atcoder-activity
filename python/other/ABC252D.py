from collections import Counter


N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
M = len(count)
B = list(count.values())
dp = [[0] * 4 for _ in range(M + 1)]

for i in range(M):
    dp[i][0] = 1
    for b in range(3):
        dp[i + 1][b + 1] = dp[i][b] * B[i] + dp[i][b + 1]

print(dp[M][3])
