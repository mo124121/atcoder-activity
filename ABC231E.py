from math import ceil

N, X = map(int, input().split())
A = list(map(int,input().split()))

a_count = [0]*N
memo ={}

def dfs(x, beg):
    if x in memo:
        return x
    if beg==N-1:
        return x//A[N-2]
    if x==0:
        return 0
    
    current = A[beg]
    next = A[beg+1]
    r = x%next/current
    ans = dfs(x/next*next,beg+1)+r

    if r:
        min(ans,dfs(ceil(x,next)*next,beg+1)+(next/current-r))
    memo[x]=ans
    return ans

print("wakarann!")