N= int(input())
C=[0]*N
P=[0]*N

sum_1 = [0]*N
sum_2 = [0]*N

for i in range(N):
    C[i],P[i]=map(int,input().split())
    if i==0:
        if C[i]==1:
            sum_1[0]=P[i]
            sum_2[0]=0
        else:
            sum_1[0]=0
            sum_2[0]=P[i]
    else:
        if C[i]==1:
            sum_1[i]=P[i]+sum_1[i-1]
            sum_2[i]=sum_2[i-1]
        else:
            sum_1[i]=sum_1[i-1]
            sum_2[i]=P[i]+sum_2[i-1]

Q=int(input())

for i in range(Q):
    L,R=map(int,input().split())
    L-=1
    R-=1
    if L==0:
        print(sum_1[R],sum_2[R])
    else:
        print(sum_1[R]-sum_1[L-1],sum_2[R]-sum_2[L-1])