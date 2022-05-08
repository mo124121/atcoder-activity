from heapq import heappop, heappush


Q = int(input())

h = []
ret = []
a = 0
for i in range(Q):
    q = input()
    if q[0] == "3":
        ret.append(heappop(h) + a)
    else:
        x = int(q[2:])
        if q[0] == "1":
            heappush(h, x - a)
        else:
            a += x

print(*ret, sep="\n")
