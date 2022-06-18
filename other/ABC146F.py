N, M = map(int, input().split())
S = input()
L = []
R = []
for i in range(N, 0, -1):
    if S[i] == "0" and S[i - 1] == "1":
        R.append(i)
    if S[i] == "1" and S[i - 1] == "0":
        L.append(i - 1)

prev = N
ret = []
for l, r in zip(L, R):
    if r - l > M:
        print(-1)
        exit()
    while prev - r >= M:
        prev -= M
        ret.append(M)

    if prev - M > l:
        ret.append(prev - r)
        prev = r
while prev >= M:
    ret.append(M)
    prev -= M
if prev > 0:
    ret.append(prev)

print(*reversed(ret))
