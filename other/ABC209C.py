N = int(input())
C = list(map(int, input().split()))
C.sort()
MOD = 10**9 + 7
ret = 1
for i, c in enumerate(C):
    ret = ret * (c - i) % MOD
print(ret)


"""

"""
