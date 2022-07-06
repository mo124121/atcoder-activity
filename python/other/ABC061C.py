from heapq import heappop, heappush


N, K = map(int, input().split())
h = []
for i in range(N):
    a, b = map(int, input().split())
    heappush(h, (a, b))

while len(h):
    a, b = heappop(h)
    K -= b
    if K <= 0:
        break
print(a)
