N,A,B = map(int, input().split())

def findSumOfDigits(n):
    sum=0
    while n>0:
        sum+=n%10
        n //=10
    return sum


count = 0
for i in range(1,N+1):
    c=findSumOfDigits(i)
    if A<=c and c<=B:
        count+=i

print(count)