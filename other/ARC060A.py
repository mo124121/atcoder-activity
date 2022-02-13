# https://atcoder.jp/contests/arc060/submissions/29248535
n, a = map(int, input().split())
X = list(map(int, input().split()))

X = [x - a for x in X]
N = 3000
from collections import defaultdict

dp = defaultdict(lambda: 0)
dp[N] = 1
for x in X:
    nx = defaultdict(lambda: 0)
    for k, v in dp.items():
        nx[k] += v
        nx[k + x] += v
    dp = nx
print(dp[N] - 1)
