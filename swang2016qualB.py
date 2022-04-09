N = int(input())
K = list(map(int, input().split()))
INF = 10**10
L = [INF] * N
L[0] = K[0]
L[N - 1] = K[N - 2]
for i in range(1, N - 1):
    L[i] = min(K[i], K[i - 1])

print(*L)
