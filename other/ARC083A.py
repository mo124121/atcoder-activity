A, B, C, D, E, F = map(int, input().split())

dp = [[0] * (3001) for _ in range(3001)]
dp[0][0] = 1

conce_r = 0
total_r = A * 100
sugar_r = 0

for total in range(1, F + 1):
    for sugar in range(total + 1):
        water = total - sugar

        if 100 * A <= total and dp[total - 100 * A][sugar]:
            dp[total][sugar] = 1
        if 100 * B <= total and dp[total - 100 * B][sugar]:
            dp[total][sugar] = 1
        if C <= total and C <= sugar and dp[total - C][sugar - C]:
            dp[total][sugar] = 1
        if D <= total and D <= sugar and dp[total - D][sugar - D]:
            dp[total][sugar] = 1

        if sugar * 100 <= water * E and dp[total][sugar] == 1 and 0 < sugar:
            conce = 100 * sugar / total
            if conce_r < conce:
                conce_r = conce
                total_r = total
                sugar_r = sugar

print(total_r, sugar_r)


"""
DPでの書き換え
"""
