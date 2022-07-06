N, K = map(int, input().split())
A = list(map(int, input().split()))

ret = 0
left = 0
right = 0
sum = A[left]
for left in range(N):
    if sum >= K:
        ret += N - right
    else:
        r = right + 1
        for r in range(right + 1, N):
            sum += A[r]
            if sum >= K:
                ret += N - r
                break
        right = r

    sum -= A[left]

print(ret)
