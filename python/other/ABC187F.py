def main():
    N, M = map(int, input().split())
    INF = N

    D = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        D[a] |= 1 << b
        D[b] |= 1 << a

    dp = [INF] * (1 << N)
    dp[0] = 0

    for bit in range(1, 1 << N):
        for j in range(N):
            if (bit >> j) & 1 == 0:
                continue
            target = bit - (1 << j)
            if dp[target] <= 1 and (D[j] & target) == target:
                dp[bit] = 1

    for bit in range(1 << N):
        b = bit
        while b:
            nb = bit - b
            dp[bit] = min(dp[bit], dp[b] + dp[nb])
            b = (b - 1) & bit

    print(dp[(1 << N) - 1])


main()

"""
解説後
bit演算の集合が大事
いくつかの段階に分けること
部分集合の部分集合をとる効率的な走査をしること
"""
