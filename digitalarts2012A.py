import re


S = input()
N = int(input())

for i in range(N):
    w = input()
    l = len(w)
    w = w.replace("*", "[a-z]")
    w = r"\b{}\b".format(w)
    S = re.sub(w, "*" * l, S)


print(S)
