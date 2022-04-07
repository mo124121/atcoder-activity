N, X = map(int, input().split())
S = input()
over_counter = 0
for c in S:
    if over_counter > 0:
        if c == "U":
            over_counter -= 1
        else:
            over_counter += 1
    else:
        if c == "U":
            X //= 2
        else:
            if X <= 10**18 // 2:
                if c == "R":
                    X = 2 * X + 1
                else:
                    X = 2 * X
            else:
                over_counter += 1

print(X)
