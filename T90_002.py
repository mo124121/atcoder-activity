H,W=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(H)]

sum_h =[0]*H
sum_w = [0]*W

for i in range(H):
    for j in range(W):
        sum_h[i]+=A[i][j]
        sum_w[j]+=A[i][j]


for i in range(H):
    ret = [0]*W
    for j in range(W):
        ret[j]= sum_h[i]+sum_w[j]-A[i][j]
    print(*ret)
