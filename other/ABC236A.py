S = input()
a, b = map(int, input().split())

ret = ""
for i in range(len(S)):
    if i + 1 == a:
        ret += S[b - 1]
    elif i + 1 == b:
        ret += S[a - 1]
    else:
        ret += S[i]

print(ret)
