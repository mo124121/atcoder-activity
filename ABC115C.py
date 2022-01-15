N,K = map(int,input().split())

h = [0]*N
for i in range(N):
    h[i]=int(input())

h.sort()

ret=1000000000
for i in range(N-K+1):
    if ret > h[i+K-1]-h[i]:
        ret = h[i+K-1]-h[i]

print(ret)