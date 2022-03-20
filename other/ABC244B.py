N = int(input())
T = input()
D = [(1, 0), (0, -1), (-1, 0), (0, 1)]

d = 0
X = 0
Y = 0
for t in T:
    if t == "S":
        X += D[d % 4][0]
        Y += D[d % 4][1]
    else:
        d += 1

print(X, Y)
