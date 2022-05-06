N = int(input())
A = [0] * (N + 1)
for i in range(N):
    A[i + 1] = int(input())

seen = set()
seen.add(1)
target = 1
i = 0
while True:
    target = A[target]
    i += 1
    if target in seen:
        print(-1)
        exit()
    if target == 2:
        print(i)
        exit()
    seen.add(target)
