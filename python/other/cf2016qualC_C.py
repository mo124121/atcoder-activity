N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
if A[0] != T[N - 1]:
    print(0)
    exit()

MOD = 10 ** 9 + 7
MAX = 10 ** 10

T = [0] + T + [MAX]
A = [MAX] + A + [0]
N += 2

pat = [1] * N
pat[0] = 1
pat[N - 1] = 1
for i in range(1, N - 1):
    if T[i] != T[i - 1]:
        pat[i] = 1
        if T[i] > A[i]:
            print(0)
            exit()
    elif A[i] != A[i + 1]:
        pat[i] = 1
        if T[i] < A[i]:
            print(0)
            exit()
    else:
        pat[i] = min(A[i], T[i])

ret = 1
for i in range(N):
    ret *= pat[i]
    ret %= MOD

print(ret)
