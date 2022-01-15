N = int(input())
A = list(map(int,input().split()))

money=1000
stock=0

i=0
while i<N-1:
    for j in range(i+1,N):
        if stock>0:
            if A[j]>=A[j-1]:
                i+=1
                continue
            else:
                money+=stock*A[i]
                stock=0
                i=j
                break
        else:
            if A[j]<=A[j-1]:
                i+=1
                continue
            else:
                stock=money//A[j-1]
                money%=A[j-1]
                i=j
                break

money+=stock*A[N-1]
print(money)
