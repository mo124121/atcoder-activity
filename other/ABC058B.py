O = input()
E = input()
ret = []
for i in range(len(E)):
    ret.append(O[i])
    ret.append(E[i])
if len(O) != len(E):
    ret.append(O[-1])
print("".join(ret))
