n = int(input())

if n==1:
    print(0)
    exit()
elif n==2:
    print(0)
    exit()
elif n==3:
    print(1)
    exit()


a1=0
a2=0
a3=1
for i in range(n-3):
    a4=(a1+a2+a3)%10007
    a1=a2
    a2=a3
    a3=a4

print(a3)