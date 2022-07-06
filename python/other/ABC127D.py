from collections import defaultdict
from email.policy import default
from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * M
C = [0] * M

A_c = defaultdict(int)
for a in A:
    A_c[a] += 1
h = []
for a, c in A_c.items():
    h.append((-a, c))
heapify(h)

for i in range(M):
    b, c = map(int, input().split())
    heappush(h, (-c, b))

ret = 0
count = 0
last = 0
while count < N:
    v, n = heappop(h)
    v = -v
    count += n
    ret += v * n
ret -= v * (count - N)
print(ret)


"""
NUM = A+C

def compress(L):
    S = sorted(set(L))
    d = dict()
    i = 0
    for s in S:
        d[s] = i
        i += 1
    return i, S, d


n, S, d = compress(NUM)
"""
