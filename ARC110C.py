N=int(input())
P=list(map(int,input().split()))
ret = []
pre=0
if P[0]==1:
    print(-1)
    exit()
    
for i in range(N):
    if P[i]==pre+1:
        for j in range(i,pre,-1):
            P[j],P[j-1]=P[j-1],P[j]
            ret.append(j)
        pre=i

if P == sorted(P) and pre==N-1:
    print(*ret,sep="\n")
else:
    print(-1)