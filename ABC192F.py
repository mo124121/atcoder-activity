N, X = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[0] * N for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            # 追加しない場合
            dp[i + 1][k][j] = max(dp[i + 1][k][j], dp[i][k][j])
            # 追加する場合
            t = dp[i][k][j] + A[i]
            dp[i + 1][k + 1][(j + A[i]) % (k + 1)] = max(
                t, dp[i + 1][k + 1][(j + A[i]) % (k + 1)]
            )

INF = 10**18
ret = INF
for i in range(1, N + 1):
    for k in range(1, i + 1):
        if dp[i][k][0] != 0:
            ret = min(ret, (X - dp[i][k][0]) // k)

print(ret)


"""
s mod k 
sを合計で調整しkの倍数になるか？

N<100
小さい N**4までいけるのでは
mod 1~Kを計算して、そこにピッタリハマるX-sがあるか？
Σ100Ciのパターンがある

dpで埋めていけばいい
dp[i][j]=i個使った時のj mod kの存在有無
なんか無駄が多そうだがいいか？
あーでもこれ過去に使ったやつは使えないのかー


dp[i][k][j]=i個目まで使った時のj mod kの存在の時の最大値


"""
