S = input()
N = len(S)

for i in reversed(range(2, N - 2 + 1, 2)):
    if S[: i // 2] == S[i // 2 : i]:
        print(i)
        exit()
