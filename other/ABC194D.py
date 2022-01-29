N=int(input())

ex=0
sum = 0
for i in range(2,N+1):
    sum+=N/(N-i+1)

print("{:.7f}".format(sum))