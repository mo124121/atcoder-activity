X,K,D=map(int,input().split())

temp =abs(X)//D
if temp > K:
    print( abs(X) -D*K)
else:
    temp = K-temp
    if temp%2==0:
        print(abs(X)%D)
    else:
        print(D-abs(X)%D)