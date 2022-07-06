N = int(input())


def S(i):
    if i == 1:
        return "1"
    else:
        return S(i - 1) + " " + str(i) + " " + S(i - 1)


print(S(N))
