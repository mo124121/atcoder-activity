T = int(input())

A = "atcoder"
ret = []

for i in range(T):
    S = input()
    if S == "a" * len(S):
        ret.append(-1)
        continue
    if A < S:
        ret.append(0)
    else:
        for i in range(len(S)):
            if ord("a") < ord(S[i]) <= ord("t"):
                ret.append(i)
                break
            elif ord(S[i]) > ord("t"):
                ret.append(i - 1)
                break
print(*ret, sep="\n")
