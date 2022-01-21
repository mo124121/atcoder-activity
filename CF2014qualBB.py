N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

count = 0
for i in range(N):
    count += A[i]
    if K <= count:
        print(i + 1)
        break
