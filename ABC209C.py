N = int(input())
C = list(map(int,input().split()))

C.sort()

def func():
    count_1 = 0
    ret = 1
    for i in range(N):
        if C[i]<i+1:
            return 0
        ret *=(C[i]-i)
        ret %=(10**9+7)
        if ret == 0:
            ret = 1
    return ret

print(func())