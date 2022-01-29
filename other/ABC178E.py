N=int(input())

x=[0]*N
y=[0]*N
for i in range(N):
    x[i],y[i]=map(int,input().split())

ret=0
for i in range(N):
    for j in range(i+1,N):
        current= abs(x[i]-x[j])+abs(y[j]-y[i])
        if ret > current:
            ret=current


print(ret)
