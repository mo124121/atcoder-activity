N = int(input())

A = [0]*N
B= [0]*N

for i in range(N):
    A[i],B[i] = map(int,input().split())


ret = 0

for i in range(N):
    for j in range(N):
        l = ((A[i]-A[j])**2+(B[i]-B[j])**2)**.5
        if ret < l:
            ret=l

print(ret)