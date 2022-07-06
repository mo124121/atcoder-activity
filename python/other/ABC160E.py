X, Y, A, B, C = map(int, input().split())
Qa = list(map(int, input().split()))
Qb = list(map(int, input().split()))
Qc = list(map(int, input().split()))
Qa.sort(reverse=True)
Qa = Qa[:X]
Qb.sort(reverse=True)
Qb = Qb[:Y]
Qc.sort()

ret = sum(Qa) + sum(Qb)
INF = 10**18
while len(Qc) and len(Qa) + len(Qb):
    v = Qc.pop()
    if len(Qa):
        a = v - Qa[-1]
    else:
        a = -INF

    if len(Qb):
        b = v - Qb[-1]
    else:
        b = -INF

    if a > 0 or b > 0:
        if a >= b:
            ret += v - Qa.pop()
        else:
            ret += v - Qb.pop()
    else:
        break

print(ret)
"""
A,B<10**5

こらまたDPっぽい
そうでもないか？
X<A
Y<B
の時点で、色を変えなくてもいい

まずはQはおいしい降順でソートでいい
もしかすると全部まとめてソートかも

AとB、どちらに変えたほうがいいかのロジックは？
何個まで入れられるか？

とりあえず、上位X,Y個のリストを作る
それぞれにbisectで挿入を試みつつ、
入れられそうなら改善量が高いほうに突っ込んでいく

AC

解説
AとBのやつの累積和とCの累積和で
ベストな和を探す
ポイントはA＆Bのやつを減らす行為はCを増やす行為に相当すること
"""
