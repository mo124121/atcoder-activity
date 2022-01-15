L,R=map(int,input().split())
MOD=2019
l = L % MOD
r = R % MOD

if r<=l:
    print(0)
elif R - L >= 2019:
    print(0)
else:
    ret=MOD**2
    for i in range(l,r):
        for j in range(i+1,r+1):
            buf = (i*j)%MOD
            if ret> buf:
                ret=buf
    print(ret)