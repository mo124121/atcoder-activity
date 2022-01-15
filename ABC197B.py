H,W,X,Y=map(int,input().split())
S=[list(input()) for  _ in range(H)]

ret=1
for move in (-1,1):
    current_x=X-1
    current_y=Y-1
    while True:
        current_x+=move
        if not (0<=current_x<H):
            break
        if S[current_x][current_y]=="#":
            break
        ret+=1


for move in (-1,1):
    current_x=X-1
    current_y=Y-1
    while True:
        current_y+=move
        if not (0<=current_y<W):
            break
        if S[current_x][current_y]=="#":
            break
        ret+=1

print(ret)