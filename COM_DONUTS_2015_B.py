N,M=map(int,input().split())
A=list(map(int,input().split()))

B=[0]*M
C=[0]*M
I=[[] for _ in range(M)]

for i in range(M):
    hoge = list(map(int,input().split()))
    B[i]=hoge[0]
    C[i]=hoge[1]
    I[i]=hoge[2:]


def eval(idles_unit:list):
    base=0
    for idle in idles_unit:
        base+=A[idle]
    
    bonus=0
    for m in range(M):
        flag=0
        for i in range(C[m]):
            if I[m][i]-1 in idles_unit:
                flag+=1
        if flag>=3:
            bonus+=B[m]
    return base,bonus

from itertools import combinations

ret=0
for combi in combinations(range(N),9):
    
    base,bonus=eval(combi)
    score=base+bonus
    if ret<score:
        ret=score

print(ret)