N = int(input())
S = input()
MOD = 998244353
dp = [[[0] * (11) for _ in range(1 << 10)] for _ in range(N + 1)]
dp[0][0][10] = 1  # ダミーとしての11個目

for i, c in enumerate(S):
    alph = ord(c) - ord("A")
    for bit in range(1 << 10):
        for last in range(11):
            dp[i + 1][bit][last] += dp[i][bit][last]  # 選ばない場合
            if alph != last and bit & (1 << alph):  # 最後ではなく、過去に選んでる場合は遷移できない
                continue
            dp[i + 1][bit | (1 << alph)][alph] += dp[i][bit][last]
            dp[i + 1][bit | (1 << alph)][alph] %= MOD

ans = 0
for bit in range(1 << 10):
    for last in range(10):  # ダミーは含まないこと
        ans += dp[N][bit][last]
        ans %= MOD
print(ans)


"""
bitDPまでは思いついたが解説読んだ

・最後の状態を持っておいて、続けられるかどうか？
・初期値の遷移元をうまく設計できるか？（全体に配布でき、かつ増やしすぎない）
"""
