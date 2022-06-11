N=int(input())
P=list(map(int,input().split()))
I=list(map(int,input().split()))

ret=[[0]*2 for _ in range(N+1)]

seen={0:0}
i=0
j=0
Ic=I[j]
par=[0]
r_flag=0
for i,p in enumerate(P):
    if p!=Ic:
        ret[par[-1]][r_flag]=p
        par.append(p)
        seen[p]=len(par)-1
    else:
        if r_flag==0:
            r_flag=1
        else:
            