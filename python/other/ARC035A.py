S = input()

for i in range(len(S) // 2 + 1):
    if S[i] != "*" and S[-1 - i] != "*":
        if S[i] != S[-1 - i]:
            print("NO")
            exit()
print("YES")
