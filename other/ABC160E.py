X, Y, A, B, C = map(int, input().split())
Qa = list(map(int, input().split()))
Qb = list(map(int, input().split()))
Qc = list(map(int, input().split()))

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

"""
