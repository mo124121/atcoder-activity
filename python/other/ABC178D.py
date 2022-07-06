S = int(input())
L = S // 3
MOD = 10**9 + 7
dp = [[0] * (S + 1) for _ in range(L + 1)]
dp[0][0] = 1
for i in range(L):
    for j in range((i + 1) * 3, S + 1):
        dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j - 3]) % MOD

ret = 0
for i in range(L):
    ret = (ret + dp[i + 1][S]) % MOD
print(ret)


"""
dp使った数え上げに見える
S<=2000
3<=ai 最長でも2000//3=666
dp[i][j]=数字をi個使って合計jになるパターン数
ちょっと遷移多い？全てがいもすに見える
個数制限なしナップサックに近いのでは？
合計が一つ小さい数字からは必ず遷移できる

もらう方向で記載
"""
