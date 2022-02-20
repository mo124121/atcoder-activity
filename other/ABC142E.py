N, M = map(int, input().split())

A = [0] * M
b = [0] * M
C = [0] * M
for i in range(M):
    A[i], b[i] = map(int, input().split())
    tmp = map(int, input().split())
    for t in tmp:
        C[i] += 1 << (t-1)

INF=10**15
dp=[[INF]*(2**(N)) for _ in range(M+1)]
dp[0][0]=0
for i in range(M):
    for j in range(2**(N)):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        next_i= j|C[i]
        dp[i+1][next_i]=min(dp[i+1][next_i],dp[i][j]+A[i])

ret=dp[M][2**(N)-1]
if ret==INF:
    print(-1)
else:
    print(ret)

"""
考察
dpっぽい？
or計算

Nが小さい

dp[]
"""
