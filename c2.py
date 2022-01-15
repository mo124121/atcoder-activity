N,Q=map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()
for i in range(Q):
    x = int(input())
    if A[-1] < x:
        print(0)
        continue
    diff = int((N+1)/2)
    i = diff
    while True:
        diff = int(diff/2)
        if diff == 0:
            print(i+1)
            break
        if A[i]>x:
            i += diff
        else:
            i -= diff
