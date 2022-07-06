N, D = map(int, input().split())
MOD = 998244353

two = [1] * (N + 1)
for i in range(N):
    two[i + 1] = two[i] * 2 % MOD
ans = 0
for i in range(D + 1):
    j = D - i
    if i >= N:
        continue
    if j >= N:
        continue
    now = two[N - max(i, j)] - 1
    now = two[max(i - 1, 0)] * now % MOD
    now = two[max(j - 1, 0)] * now % MOD
    ans += now
    ans %= MOD


print(ans * 2 % MOD)
