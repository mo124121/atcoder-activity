T = int(input())
for t in range(T):
    inp = input().split()
    X = int(inp[0])
    Y = int(inp[1])
    art = inp[2]
    N = len(art)
    ret = 0
    prev = art[0]
    for i in range(1, N):
        if art[i] == "C":
            if prev == "J":
                ret += Y
            prev = art[i]
        if art[i] == "J":
            if prev == "C":
                ret += X
            prev = art[i]
    print("Case #{}: {}".format(t + 1, ret))
