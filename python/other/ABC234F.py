S=input()
MOD=998244353

from collections import defaultdict
alp_count=defaultdict(lambda:0)
for c in S:
    alp_count[c]+=1

class Binom:
    def __init__(self,size,mod) -> None:
        fac=[0]*size
        finv=[0]*size
        inv=[0]*size
        fac[0]=1
        fac[1]=1
        inv[1]=1
        finv[0]=1
        finv[1]=1
        for i in range(2,size):
            fac[i]=fac[i-1]*i%mod
            inv[i]=mod-(mod//i)*inv[mod%i]%mod
            finv[i]=finv[i-1]*inv[i]%mod
        self.fac=fac
        self.finv=finv
        self.inv=inv
    
    def calc(self,n,r):
        if n < r or n <0 or r<0:
            return 0
        else:
            return self.fac[n] * (self.finv[r]*self.finv[n-r]%MOD)%MOD


dp = [[0]*(len(S)+1) for _ in range(len(alp_count)+1)]
dp[0][0]=1
binom=Binom(len(S)+10,MOD)

for i,count in enumerate(alp_count.values()):
    for j in range(len(S)+1):
        for k in range(min(j,count)+1):
            dp[i+1][j] += dp[i][j-k]*binom.calc(j,k)%MOD
            dp[i+1][j] %=MOD

ret =0

for i in range(1,len(S)+1):
    ret+=dp[len(alp_count)][i]
    ret%=MOD

print(ret)