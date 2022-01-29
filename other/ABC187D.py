N = int(input())
vote=[[0]*2 for _ in range(N)]

sum_A=0
sum_B=0

for i in range(N):
    vote[i][0],vote[i][1]=map(int,input().split())
    sum_A+=vote[i][0]

ret=0
vote.sort(key=lambda x: x[0]*2+x[1],reverse=True)

for i in range(N):
    if sum_A<sum_B:
        break
    sum_B+=vote[i][0]+vote[i][1]
    sum_A-=vote[i][0]
    ret+=1

print(ret)