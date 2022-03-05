S = input()
Q = int(input())
S2 = [ord(S[i]) - ord("A") for i in range(len(S))]
ABC = "ABC"
ret = []
for i in range(Q):
    t, k = map(int, input().split())
    k -= 1
    if t == 0:
        ret.append(S[k])
        continue
    elif t <= 60:
        root = k // (1 << t)
    else:
        root = 0
    j = 0
    shift = 0
    for j in range(60):
        if j >= t:
            break
        if 1 & k >> j:
            shift += 1
        else:
            shift += 0
    ret.append(ABC[(S2[root] + shift + t) % 3])

print(*ret, sep="\n")
