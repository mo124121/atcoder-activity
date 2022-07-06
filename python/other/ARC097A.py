from heapq import heapify, heappop, heappush


s = input()
K = int(input())
if len(s) == 1:
    print(s)
    exit()

h = []
heapify(h)
n = len(s)
seen = {}
for i in range(n):
    for j in range(i + 1, min(i + 1 + K, n + 1)):
        t = s[i:j]
        if t not in seen:
            heappush(h, s[i:j])
            seen[t] = True
ret = ""

for i in range(K):
    ret = heappop(h)

print(ret)
