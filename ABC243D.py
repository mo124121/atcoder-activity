N, X = map(int, input().split())
S = input()

d = 0
X_s = list(bin(X))
for c in S:
    if c == "U":
        X_s.pop()
    elif c == "L":
        X_s.append("0")
    else:
        X_s.append("1")


print(int("".join(X_s), 0))
