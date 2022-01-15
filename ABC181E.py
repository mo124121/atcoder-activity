N,M=map(int,input().split())
H = list(map(int,input().split()))
W = list(map(int,input().split()))

diff1=[0]*((N-1)/2)
diff2=[0]*((N-1)/2)
for i in len(diff1):
    diff1[i]=H[2*i+1]-H[2*i]
    diff2[i]=H[2*i+2]-H[2*i]