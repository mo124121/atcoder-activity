from collections import deque


N, M, Q = map(int, input().split())

abcd = [tuple(map(int, input().split())) for _ in range(Q)]

pat = [[1]]
ret = 0
x = 0
while len(pat):
    p = pat.pop()
    if len(p) <= N:
        for i in range(p[-1], M + 1):
            pat.append(p + [i])
    else:
        x += 1
        r = 0
        for j in range(Q):
            a, b, c, d = abcd[j]
            if p[b] - p[a] == c:
                r += d
        ret = max(ret, r)

print(ret)

"""
abcd.sort(key=lambda x: x[1])

dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(M):
        for k in range(Q):
            a,b,c,d=abcd[k]
            if a==j:
"""


"""
考察
N,M<10
Q<50
小さい
2^NとかN!ぐらいはいけそう

全探索だとM^Nになる？ちょっとあやしい
ただ後半は小さそう、微妙なライン

すごいDPっぽい　なぜDPっぽい？　→　行ったり来たりがないから　一方向の操作でいい

dp[最大値X]=最大値Xまで使ってとれるスコア x

味方に寄っては納期がある仕事の類似問題　あとのほうでソートする x
なんか微妙に違いそう？
Nはヒットポイントみたいな感じ　なるべく使わないで高スコアな方がいい
Aaiが前のAbiだと使用が少なくなる

dp[最大値X][使用数Y]=Y個数字を使って最大値Xまで使ってとれるスコア 

誤読乙

ある番目からある番目の差がci
dp[最大値X]=最大値Xまで使ってとれるスコア

やっぱり何か違う…

条件を満たす、ということはどういうことか？
A3-A1=5 -> (A1,A3)=(1,6),(2,7),(3,8),(4,9),(5,10)

やっぱり全探索のほうが筋がよさそう

"""
