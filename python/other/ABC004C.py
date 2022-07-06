N = int(input())
N %= 30
S = [1, 2, 3, 4, 5, 6]

for i in range(N):
    i %= 5
    S[i], S[i + 1] = S[i + 1], S[i]

print(*S, sep="")
