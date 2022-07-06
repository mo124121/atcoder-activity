N = int(input())
S = list(map(int, input().split()))

x = [0, 0]

for s in S:
    x.append(s - x[-1] - x[-2])

c0 = max([-x[i] for i in range(0, N + 2, 3)])
c1 = max([-x[i] for i in range(1, N + 2, 3)])
c2 = min([x[i] for i in range(2, N + 2, 3)])

if c0 + c1 > c2:
    print("No")
    exit()
print("Yes")

A = [c0, c1]
for s in S:
    A.append(s - A[-1] - A[-2])

print(*A)
