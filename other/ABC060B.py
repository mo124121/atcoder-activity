a,b,c=map(int,input().split())

ret="NO"

for i in range(1,101):
    if (a*i)%b==c:
        ret="YES"
        break

print(ret)