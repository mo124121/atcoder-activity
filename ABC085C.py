N,Y = map(int,input().split())

d=-1
e=-1
f=-1
for a in range(N+1):
    for b in range(N+1-a):
        c=N-a-b
        total = a*10000+b*5000+c*1000
        if total==Y:
            d=a
            e=b
            f=c

print(d,e,f)