N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

c_m = 0
c_p = 0
dp = [[0] * 2 for _ in range(N)]
dp[0][0] = A[0]

for i in range(1, N):
    dp[i][0] += dp[i - 1][0] + A[i]
    if i != 1:
        dp[i][0] += dp[i - 1][1] + A[i]
    dp[i][1] += dp[i - 1][0] - A[i]
    dp[i][0] %= MOD
    dp[i][1] %= MOD

print(dp[N - 1][0] + dp[N - 1][1])


"""
長さを増しながらDPっぽくはある
N<10**5

前がマイナスな場合とそうじゃない場合で遷移をかえればいい

問題は加算量
ある番目の文字を伸ばすことでの加算量は、
それまでのパターン数かけた量

都度のパターン数を保持しておいたらいい？


"""
