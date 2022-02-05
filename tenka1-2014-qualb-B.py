N=int(input())
S=input()
T=[]
for i in range(N):
    T.append(input())

MOD=1000000007

dp = [0]*(len(S)+1)
dp[0]=1

for i in range(len(S)+1):
    for phrase in T:
        l=len(phrase)
        if i>=l:
            if phrase==S[i-l:i]:
                dp[i]+=dp[i-l]
    dp[i]%=MOD

print(dp[len(S)])
