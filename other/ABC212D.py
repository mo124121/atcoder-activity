from heapq import heappop, heappush


Q = int(input())
a = 0
h = []
ret = []
for i in range(Q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        heappush(h, t[1] - a)
    elif t[0] == 2:
        a += t[1]
    else:
        ret.append(heappop(h) + a)
print(*ret, sep="\n")
