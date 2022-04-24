T = int(input())
ret = []
for t in range(T):
    N, A, B, X, Y, Z = map(int, input().split())

    if Y >= A * X and Z >= B * X:
        ret.append(N * X)
        continue

    if A * Z < B * Y:  # A/Y<B/Z
        A, Y, B, Z = B, Z, A, Y

    r = N // A * Y + (N - N // A * A) * X
    # Bがでかいパターン
    if B**B > N:
        for i in range(1, N // B + 2):
            Ni = N - i * B
            ri = Ni // A * Y + i * Z + (Ni - Ni // A * A) * X
            r = min(r, ri)
    # そうでもないパターン
    else:
        seen = {}
        for i in range(N // A, -1, -1):
            Ni = N - i * A
            xc = Ni - Ni // B * B
            if xc in seen:
                break
            ri = i * Y + Ni // B * B * Z + xc * X
            r = min(r, ri)
            seen[xc] = True

    ret.append(r)

print(*ret, sep="\n")


"""
dpで先にテーブル作っておく感じや！
N<10**9　テーブルは作れない！残念！
都度AもBも違うので再利用できないしね…

とにかくdpっぽくはあるが、
数字がいずれも大きいのでできない

3つの選択肢がある中でどうするか？
効率がいい選択肢を重視しつつ、ピッタリ当てはめる

まずできるのはN*Xで必ず到達できる

x+Ay+Bz==N
x>=0
y>=0
z>=0
これはxを調整すれば必ず達成できる



1/Xのコスパがいい時->N*X
A/Yのコスパがいい時->y=(N-x-Bz)//A N-x-Bzがどういう数字をとるか次第、クソややこしい

Ay=x+Bzとなるケースもあって、状況的には効率的になる可能性がある？


まあとりあえず書いていく
一応パターン分けでサンプルは通るが本当にこれでいい？
たぶんWAだが出す


ただ、この手の奴はパターンがあって定石は別にありそう

結局、残ったところでDPするしかないのでは？

効率順として
x>y,z N*X
y>x>z a*y+(N-a*y)*x

y>z>x このケースがややこしい　
xはなるべく使いたくないが、yを減らしてまで効率があげられる範囲はどこか？

yyyyy yyyyy yyyyy xxxx
yyyyy zzzzzzzzzzzzz x

A<Bは言えそう、いや必ずしもそうは言えない？

yy yy x
yy zzz

yを減らして行ったときに、xの個数パターンが変動するはず
そこが網羅されればいい…けどz<10**9なのよね…


まだ30分ある、少し考え直す
T<100
*<10**9
sqrt(N)あたりはたたいてもいい
クエリ先読みの可能性はあるか？ ->　パラメータが異なる以上、流用はできない

yとzの個数の関係性について
xの出るパターンはBだけある->zが大きい時 逆に全パターンできるのでは？
B**2>N 全列挙
B**2<N yの個数でmodをとるイメージ




"""
