T = int(input())
for t in range(T):
    ret = 0
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    for i in range(N):
        if ret < S[i]:
            ret += 1
    print("Case #{}: {}".format(t + 1, ret))
