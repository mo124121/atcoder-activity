N = int(input())

XYZ = []
for i in range(N):
    XYZ.append(tuple(map(int, input().split())))

D = [[0] * N for _ in range(N)]

for i in range(N):
    x, y, z = XYZ[i]
    for j in range(N):
        xn, yn, zn = XYZ[j]
        D[i][j] = abs(x - xn) + abs(y - yn) + max(0, z - zn)

INF = 10**18
dp = [[INF] * (2**N) for _ in range(N)]


"""
Nが小さい
N<=17

各距離マトリックス出してダイクストラでいいはず
Zが特殊だが、これも双方向違うコストがあるという感覚でいいはず

都市1に戻ってくる…？ていうか全部通る…？
ダイクストラではない

候補はN! 最後に帰ってくるコスト

そのままだと巡回セールスマン問題でNPなんちゃら

2点間の移動はどこも経由しないのが最短経路
最短の経路を貪欲にとっていくのがベスト？

二点間の距離は高さ要素を除けば同じ

2**N<1.3*10**6

通った場所、最後の場所で考える？

区間かbitDPっぽいんだよなあ

解説後
やはりbit DP
"""
