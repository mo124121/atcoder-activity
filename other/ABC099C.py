N = int(input())

D = [1]

d = 6
while d <= 10**5:
    D.append(d)
    d *= 6
d = 9
while d <= 10**5:
    D.append(d)
    d *= 9

D.sort()
INF = 10**6
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(1, N + 1):
    for d in D:
        if i - d >= 0:
            dp[i] = min(dp[i], dp[i - d] + 1)

print(dp[N])

"""
考察
全部の金額列挙してサーチする？
ソートして大きい方貪欲に引いているとか？
その場合逆転はない？大丈夫？

なんかdpくさい
ある数字が作れる最小回数　的な

"""
