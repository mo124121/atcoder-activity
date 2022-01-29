N = int(input())
count={}

for i in range(N):
    name=input()
    if name in count:
        count[name]+=1
    else:
        count[name]=1

print(max(count,key=count.get))