N,M = map(int,input().split())

parent = [-1]*N
child = [N+1]*N

for i in range(M):
    A,B=map(int,input().split())
    parent[B-1]=A-1
    child[A-1]=B-1
    
