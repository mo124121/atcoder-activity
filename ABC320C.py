n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

ret = [["."]*(s-r+1) for _ in range(q-p+1)]

left = max(p-a,r-b)
right = min(q-a,s-b)

for k in range(left,right+1):
    ret[a+k-p][b+k-r]="#"

left = max(p-a,b-s)
right = min(q-a,b-r)

for k in range(left,right+1):
    ret[a+k-p][b-k-r]="#"

for line in ret:
    print("".join(line))