from collections import Counter


N = int(input())
S = input()
T = input()

if Counter(S)["0"] != Counter(T)["0"]:
    print(-1)
    exit()


def indices(X):
    Xi = []
    for i, c in enumerate(X):
        if c == "0":
            Xi.append(i)
    return Xi


Si = indices(S)
Ti = indices(T)
ret = 0
for s, t in zip(Si, Ti):
    ret += int(s != t)
print(ret)
