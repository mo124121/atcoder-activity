N, K = map(int, input().split())
dp = [K] * N
MOD = 998244353
for i in range(K):
    c, k = input().split()
    k = int(k)
    if c == "L":
        for i in range(k - 1):
            if dp[i] != 1:
                dp[i] -= 1
        dp[k - 1] = 1
    else:
        dp[k - 1] = 1
        for i in range(k, N):
            if dp[i] != 1:
                dp[i] -= 1

ret = 1
for d in dp:
    ret = ret * d % MOD
print(ret)
