N = int(input())
S = input()

if N % 2 != 0:
    print(-1)
    exit()
ret = 0
for i in range(N // 2):
    if S[i] != S[i + N // 2]:
        ret += 1

print(ret)
