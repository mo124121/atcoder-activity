N,M =map(int,input().split())

conne = [[False]*N for _ in range(N)]
for i in range(M):
    x,y =map(int,input().split())
    conne[x-1][y-1]=True

ret = 1
import itertools
for pattern in itertools.product([0,1],repeat=N):
    habatsu_pat = []
    for i in range(len(pattern)):
        if pattern[i]==1:
            habatsu_pat.append(i)

    flag = True
    for j in itertools.combinations(list(habatsu_pat),2):
        if conne[j[0]][j[1]]:
            continue
        else:
            flag = False
            break
    if flag and ret < len(habatsu_pat):
        ret=len(habatsu_pat)

print(ret)
        