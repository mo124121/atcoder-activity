N = int(input())
A = [int(i) for i in input().split()]

flag =True
count = 0
while flag:
    for a in A:
        if a % 2 != 0:
            flag=False
            count -=1
            break
    A = [i//2 for i in A]
    count +=1

print(count)