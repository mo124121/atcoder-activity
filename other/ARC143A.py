A = list(map(int, input().split()))
A.sort(reverse=True)

ret = 0

op = A[1] - A[2]
A[0] -= op
A[1] -= op
ret += op

if A[0] > 2 * A[1]:
    print(-1)
    exit()
op = A[0] - A[1]
A[0] -= 2 * op
A[1] -= op
A[2] -= op
ret += 2 * op

op = A[0]
ret += op

print(ret)
