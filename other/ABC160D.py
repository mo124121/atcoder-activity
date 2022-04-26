N, X, Y = map(int, input().split())
X -= 1
Y -= 1
ret = [0] * N


for i in range(N - 1):
    for j in range(i + 1, N):
        ret[min(j - i, abs(i - X) + 1 + abs(j - Y))] += 1

print(*ret[1:], sep="\n")


"""
直線+どっかがつながっているグラフ

N<2*10**3　微妙に小さい
N**2log(N)とかは行けそうN**3はつらい

順次幅探索をしていけば良い
ワーシャルフロイド?

解説後
言われてみれば確かにそう

"""
