T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ret = 0
    for i in range(N - 1):
        for j in range(i, N):
            if A[j] == i + 1:
                break
        B = A[i : j + 1]
        for k, b in enumerate(reversed(B)):
            A[i + k] = b
        ret += len(B)
    print("Case #{}: {}".format(t + 1, ret))
