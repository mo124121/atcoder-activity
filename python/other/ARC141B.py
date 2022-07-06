from itertools import combinations

MOD = 998244353


def solve(N, M):

    for bits in range(61):
        if 1 << bits > M:
            break
    if bits < N:
        return 0

    dp = [[0] * bits for _ in range(N)]
    for i in range(bits):
        dp[0][i] = 2**i
    dp[0][bits - 1] = M - (2**i - 1)
    for i in range(N - 1):
        for j in range(bits - 1):
            for k in range(j + 1, bits):
                dp[i + 1][k] += dp[i][j]
                dp[i + 1][k] %= MOD
        for k in range(bits):
            dp[i + 1][k] *= dp[0][k]
            dp[i + 1][k] %= MOD

    return sum(dp[N - 1]) % MOD


def main():
    N, M = map(int, input().split())

    ret = solve(N, M)
    print(ret)


main()


def naive(N, M):
    ret = 0
    for pat in combinations(range(1, M + 1), N):
        pre = 0
        flag = True
        for p in pat:
            b = pre ^ p
            if pre >= b:
                flag = False
                break
            pre = b
        if flag:
            ret += 1
    return ret


M = 15
for i in range(1, M + 1):
    print(i, naive(i, M), solve(i, M))

"""
DPっぽくはあるがどう構成するか


bit以上のものしか立てられない
DPや
"""
