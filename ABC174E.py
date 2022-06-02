from heapq import heapify, heappop, heappush


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
h = [(-a, 1) for a in A]

heapify(h)

while K > 0:
    if len(h) == 1:
        v, c = heappop(h)
        if c <= K:
            heappush((v / 2, c * 2))
            K -= c
        else:
            heappush((v / 2, K * 2))
            heappush((v, c - K))
            K = 0
        continue

    v1, c1 = heappop(h)
    v2, c2 = heappop(h)
    if c1 <= K:
        if v1 / 2 > v2:
            heappush(h, (v2, c1 + c2))
            heappush(h, (v1 - v2, c1))
        else:
            heappush(h, (v2, c2))
            heappush(h, (v1 / 2, c1 * 2))
        K -= c1
    else:
        heappush(h, (v1, c1 - K))
        heappush(h, (v2, K + c2))
        heappush(h, (v1 - v2, K))
        K = 0
v, c = heappop(h)
print(f"{-v:.7f}")
