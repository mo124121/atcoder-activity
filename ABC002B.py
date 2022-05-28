W = input()
ret = []
for c in W:
    if c not in "aiueo":
        ret.append(c)
print(*ret, sep="")
