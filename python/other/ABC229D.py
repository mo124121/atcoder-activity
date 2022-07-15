S = input()
K = int(input())


r = 0
ret = 0
for l in range(len(S)):
    while K >= 0 and r < len(S):
        if S[r] == ".":
            if K == 0:
                break
            K -= 1
        r += 1
    ret = max(ret, r - l)
    if S[l] == ".":
        K += 1

print(ret)
