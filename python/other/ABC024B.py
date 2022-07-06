N, T = map(int, input().split())
prev = -1
count = 0
for _ in range(N):
    A = int(input())

    count += T - max(0, prev - A)

    prev = A + T
print(count)
