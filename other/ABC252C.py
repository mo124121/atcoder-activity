N = int(input())
S = [input() for _ in range(N)]
count = [[0] * 10 for _ in range(10)]

for s in S:
    for i, d in enumerate(s):
        d = int(d)
        count[d][i] += 1

ret = 10**10

for d in range(10):
    r = 0
    max_count = 0
    for i in range(10):
        if count[d][i] >= max_count:
            r = i + (count[d][i] - 1) * 10
            max_count = count[d][i]
    ret = min(ret, r)


print(ret)
