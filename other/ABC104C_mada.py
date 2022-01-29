D,G = map(int,input().split())
P = [0]*D
C = [0]*D


MAX_SCORE = 0
MAX_COUNT = 0
for i in range(D):
    P[i],C[i]=map(int,input().split())
    C[i]//=100
    MAX_SCORE+=P[i]+C[i]
    MAX_COUNT+=P[i]

#dp = [[MAX_COUNT]*(MAX_SCORE+1+10**4+10) for _ in range(D+1)]
dp = [[MAX_COUNT]*(401010) for _ in range(D+1)]
dp[0][0] = 0
for i in range(D):
    for point in range((201010)):
        for j in range(P[i]):
            if dp[i+1][point+(i+1)*j]>dp[i][point]+j:
                dp[i+1][point+(i+1)*j]=dp[i][point]+j
        if dp[i+1][point+(i+1)*P[i]+C[i]]>dp[i][point]+P[i]:
            dp[i+1][point+(i+1)*(P[i])+C[i]]=dp[i][point]+P[i]

ret = MAX_SCORE

for point in range(G//100,(MAX_SCORE)):
    if ret > dp[D][point]:
        ret =dp[D][point]

print(ret)








# def dfs_dame(score,count,i):
#     if i==D:
#         # print(score,count )
#         return score,count
#     else:
#         best_count = INF_COUNT
#         score_current = 0

#         for j in range(P[i]+1):
#             s,c=dfs_dame(score+j*(i+1)*100+(j//P[i])*C[i],count+j,i+1)
#             if s>=G and c<best_count:
#                 best_count= c
#                 score_current = s

#         return score_current,best_count

# _,ret = dfs_dame(0,0,0)