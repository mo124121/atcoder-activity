def gcd(a,b):
    c = a%b
    if c==0:
        return b
    else:
        return gcd(b,c)


A,B,C=map(int,input().split())

r = gcd(A,gcd(B,C))

print((A+B+C)//r-3)