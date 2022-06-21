T = int(input())
ans = []
MOD = 998244353
for t in range(T):
    N = int(input())
    S = input()
    T = S[: (N + 1) // 2]
    r = 0
    best = T + T[::-1][N % 2 :]
    if S >= best:
        r += 1
    i = 0
    for c in reversed(T):
        r += pow(26, i, MOD) * (ord(c) - ord("A"))
        r %= MOD
        i += 1
    ans.append(r)

for a in ans:
    print(a)
