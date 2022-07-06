N, Q = map(int, input().split())
S = input()
l = [0] * Q
r = [0] * Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())

at_count = [0] * N

for i in range(N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        at_count[i + 1] = at_count[i] + 1
    else:
        at_count[i + 1] = at_count[i]

ret = []
for i in range(Q):
    ret.append(at_count[r[i] - 1] - at_count[l[i] - 1])


print(*ret, sep="\n")
