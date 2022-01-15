N=int(input())

ret=0

x=[0]*N
y=[0]*N

for i in range(N):
    x[i],y[i]=map(int,input().split())

for i in range(N):
    for j in range(i+1,N):
        l = ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
        if ret<l:
            ret=l

print("{:.6f}".format(ret))