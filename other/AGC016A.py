from collections import defaultdict


S = input()
if S == S[0] * len(S):
    print(0)
    exit()
S2 = list(S)
ret = 1000
for i in range(26):
    c = chr(ord("a") + i)
    S3 = S2.copy()
    t = 0
    while True:
        N = len(S3)
        S4 = []
        for i in range(N - 1):
            if c in S3[i : i + 2]:
                S4.append(c)
            else:
                S4.append(S3[i])
        S3 = S4
        t += 1
        flag = True
        for s in S3:
            if s != c:
                flag = False
                break
        if flag:
            break
    ret = min(ret, t)

print(ret)
