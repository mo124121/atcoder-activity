N,K=map(int,input().split())
D=list(map(int,input().split()))

add = [0]*10
for i in range(10):
    if i in D:
        



ret = N
keta=1
current=0
while True:
    current = (ret%(10**keta))//(10**(keta-1))
    for d in D:
        if current == d:
            current+=1
            ret+=10**(keta-1)
    if ret<10**(keta):
        break
    keta+=1

print(ret)

#Nが小さいので10Nまでで全探索でよい