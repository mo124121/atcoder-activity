N, X = map(int, input().split())
S = input()

d = 0

for c in S:
    if c == "U":
        if d == 0:
            X //= 2
        else:
            d -= 1
    else:
        if X <= 10**18:
            if c == "L":
                X = X * 2
            else:
                X = X * 2 + 1
        else:
            d += 1

print(X)
