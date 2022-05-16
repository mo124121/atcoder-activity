from collections import Counter, defaultdict

N, K = map(int, input().split())
S = input()

INF = 10**4
ret = N

for l in range(1, N):
    if N % l != 0:
        continue
    counts = defaultdict(lambda: defaultdict(int))
    for i, c in enumerate(S):
        counts[i % l][c] += 1
    ops_min = 0
    for i in range(l):
        most = 0
        for v in counts[i].values():
            most = max(most, v)
        ops_min += N // l - most
    if ops_min <= K:
        print(l)
        exit()
print(N)
