N = int(input())
S = list(map(int, input().split()))

x = [0] * (N + 2)
x[0] = x[1] = 0
for i in range(N):
    x[i + 2] = S[i] - x[i + 1] - x[i]

c = [0] * 3
for i in range(3):
    c[i] = -min(x[i::3])

if c[0] + c[1] > -c[2]:
    print("No")
    exit()

add = [c[0], c[1], -c[0] - c[1]]

A = [xi + add[i % 3] for i, xi in enumerate(x)]
print("Yes")
print(*A)
