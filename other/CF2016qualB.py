N, A, B = map(int, input().split())
S = input()
YES = "Yes"
NO = "No"
a = 0
b = 0
ret = []
for s in S:
    if s == "a":
        if a + b < A + B:
            a += 1
            ret.append(YES)
        else:
            ret.append(NO)
    elif s == "b":
        if a + b < A + B and b < B:
            b += 1
            ret.append(YES)
        else:
            ret.append(NO)
    else:
        ret.append(NO)

print(*ret, sep="\n")
