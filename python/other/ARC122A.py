N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

c_p = A[0]
c_m = 0

dp = [[0] * 2 for _ in range(N)]
dp[0][0] = 1

for i in range(1, N):
    c_p, c_m = (
        c_p + c_m + A[i] * (dp[i - 1][0] + dp[i - 1][1]) % MOD,
        c_p - A[i] * (dp[i - 1][0]) % MOD,
    )
    dp[i][0] += dp[i - 1][0]
    dp[i][0] += dp[i - 1][1]
    dp[i][1] += dp[i - 1][0]
    dp[i][0] %= MOD
    dp[i][1] %= MOD

print((c_p + c_m) % MOD)


"""
長さを増しながらDPっぽくはある
N<10**5

前がマイナスな場合とそうじゃない場合で遷移をかえればいい

問題は加算量
ある番目の文字を伸ばすことでの加算量は、
それまでのパターン数かけた量

都度のパターン数を保持しておいたらいい？


解説後
dpと加算量を別で管理するのがミソ
dpはパターン数の増加=その時にAを足しこむ量を定める

過去の加算量は
一度組み込まれてしまえばパターンの増加にしたがって増えていく

"""