N,K=map(int,input().split())
P=list(map(int,input().split()))

import heapq

hq=[]

for i in range(K):
    heapq.heappush(hq,P[i])

ret=heapq.heappop(hq)
print(ret)
for i in range(K,N):
    if ret<P[i]:
        heapq.heappush(hq,P[i])
        ret=heapq.heappop(hq)
    print(ret)
