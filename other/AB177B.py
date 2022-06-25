S = input()
T = input()

ret = len(T)
for i in range(len(S) - len(T) + 1):
    c = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            c += 1
    ret = min(ret, c)
print(ret)
