n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10**9 + 7

ret_x = 0
cum_x = X[0]
for i, x in enumerate(X[1:]):
    ret_x += (i + 1) * x - cum_x
    cum_x += x
    ret_x %= MOD
    cum_x %= MOD

ret_y = 0
cum_y = Y[0]
for i, y in enumerate(Y[1:]):
    ret_y += (i + 1) * y - cum_y
    cum_y += y
    ret_y %= MOD
    cum_y %= MOD

print(ret_x * ret_y % MOD)
