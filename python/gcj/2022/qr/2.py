T = int(input())
C = [0] * 3
M = [0] * 3
Y = [0] * 3
K = [0] * 3
ret = []
for t in range(T):
    for i in range(3):
        C[i], M[i], Y[i], K[i] = map(int, input().split())
    A = [0] * 4
    A[0] = min(C)
    A[1] = min(M)
    A[2] = min(Y)
    A[3] = min(K)
    r = "Case #{}: ".format(t + 1)
    if 10**6 <= sum(A):
        for i in range(len(A)):
            diff = sum(A) - 10**6
            if diff > 0:
                A[i] = max(0, A[i] - diff)
        r += "{} {} {} {}".format(*A)
    else:
        r += "IMPOSSIBLE"
    ret.append(r)

print(*ret, sep="\n")
