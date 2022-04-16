N = int(input())
A = list(map(int, input().split()))


ret = 0
b = 1
for i in range(N):
    ret += A[i] * (1 << (N - 1 - i))
print(ret)
