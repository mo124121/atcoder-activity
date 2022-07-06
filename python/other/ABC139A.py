S = input()
T = input()
ret = 0
for i in range(3):
    ret += int(S[i] == T[i])
print(ret)
