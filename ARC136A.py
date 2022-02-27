N = int(input())
S = list(input())
ret = []
i = 0
while i < N - 1:
    if S[i] == "B" and S[i + 1] == "B":
        ret.append("A")
        i += 2
    elif S[i] == "B" and S[i + 1] == "A":
        ret.append("A")
        S[i + 1] = "B"
        i += 1
    else:
        ret.append(S[i])
        i += 1
if i == N - 1:
    ret.append(S[N - 1])

print("".join(ret))
