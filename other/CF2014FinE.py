N=int(input())
R=list(map(int,input().split()))
if N<=2:
    print(0)
else:
    ret=0
    neutral = True
    for i in range(N-1):
        if R[i+1]==R[i]:
            continue
        elif neutral:
            neutral=False
            ascent = R[i+1]>R[i]


        if ascent and ((R[i+1]-R[i]) < 0):
            ret+=1
            ascent=False
        elif (not ascent) and ((R[i+1]-R[i]) > 0):
            ret+=1
            ascent=True
    if ret>0:
        ret+=2

    print(ret)