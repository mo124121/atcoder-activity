T = int(input())

for t in range(T):
    S = list(input())
    N = len(S)
    c = 0
    for i in range(N - 1):
        if S[i] < S[i + 1]:
            S[i] = S[i] * (1 + 1 + c)
            c = 0
        elif S[i] == S[i + 1]:
            c += 1
        else:
            c = 0

    print("Case #{}: {}".format(t + 1, "".join(S)))
