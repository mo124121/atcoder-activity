N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
if 0 in S:
    print(N)
    exit()

pro = 1
ret = 0

r = 0
for l in range(N):
    if l >= r:
        r = l
        pro = 1
    while pro <= K and r < N:
        pro *= S[r]
        r += 1
    if pro <= K:
        ret = max(ret, r - l)
    else:
        ret = max(ret, r - l - 1)
    pro //= S[l]

print(ret)
