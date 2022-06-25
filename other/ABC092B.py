N = int(input())
D, X = map(int, input().split())

for i in range(N):
    a = int(input())
    d = 1
    while d <= D:
        X += 1
        d += a

print(X)
