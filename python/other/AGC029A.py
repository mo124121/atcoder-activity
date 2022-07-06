S = list(input())
N = len(S)
left = 0

for i in range(N):
    left = i
    if S[i] == "B":
        break

ret = 0
for i in range(left, N):
    if S[i] == "W":
        ret += i - left
        left += 1

print(ret)
