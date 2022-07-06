N=int(input())
P=tuple(map(int,input().split()))
Q=tuple(map(int,input().split()))

import itertools
if P > Q:
    big = P
    small =Q
else:
    big = Q
    small = P

count=0
for pattern in itertools.permutations(range(1,N+1)):
    if small < pattern <=big:
        count +=1

print(count)