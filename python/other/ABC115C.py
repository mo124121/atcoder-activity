N, K = map(int, input().split())
H = [int(input()) for _ in range(N)]
H.sort()
ret = 10**18
for i in range(N - K + 1):
    ret = min(ret, H[i + K - 1] - H[i])

print(ret)
