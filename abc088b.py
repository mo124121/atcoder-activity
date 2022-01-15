N= int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

ret =0
b=1
for a in A:
    ret += b*a
    b*=-1

print(ret)