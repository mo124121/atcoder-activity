from collections import Counter, defaultdict


N = int(input())
A = list(map(int, input().split()))

ret = N * (N - 1) * (N - 2) // 6
count = Counter(A)

for k, v in count.items():
    if v == 2:
        ret -= N - 2
    elif v > 2:
        ret -= v * (v - 1) // 2 * (N - v)
        ret -= v * (v - 1) * (v - 2) // 6
print(ret)


"""

"""
