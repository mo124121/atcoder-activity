N = int(input())

t = [0]*N

for i in range(N):
    t[i]=int(input())

import itertools

ret = 150
if N==1:
    print(t[0])
else:
    for i in range(1,N):
        for baker1 in itertools.combinations(range(N),i):
            baker2 = set(i for i in range(N)) - set(baker1)
            total = max(sum([t[j] for j in baker1]),sum(t[j] for j in baker2))
            if ret > total:
                ret=total

    print(ret)