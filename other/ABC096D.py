N = int(input())
M = 55555 * 5
base = list(range(2, M + 1))
primes = list()
while base[0] ** 2 <= M:
    tmp = base[0]
    primes.append(tmp)
    base = [e for e in base if e % tmp != 0]
primes += base
primes_set = set(primes)
sum_values = [set() for _ in range(5)]
ret = []
for p in primes:
    if p % 5 == 1:
        ret.append(p)
    if len(ret) == N:
        print(*ret)
        exit()


"""
素数列挙したうえで全探索？→　直観的すぎる
全探索は厳しい

合成数=素数じゃない数

N<55 小さい

全ビットで5の倍数になる合計にするとか？→どの異なる5個を選んでも、というのが厳しいか？
そういう性質とはちょっと違いそう

素数は奇数
5個なので合計は奇数　2の倍数は無理

5個の合計が素数になるケースは実は少ないのでは？

素数をsetで持つ＆4個の合計のリストを持っておいて、
増やせるのは上記4個の合計に足した時に素数にならないやつ、とか？
54C4 なりますけど大丈夫でっか？確率的にはそんな繰り返さなくていいはずだが、
これだと超える制約な気がする

全パターンじゃなくて、setで管理するなら問題なさそう、行ける
各合計個数のとりうる値をsetで管理

ん？2入れたら絶対偶数になるんじゃね？合成数じゃね？->だから全パターンなんで…


実装してみたが、遅い&数字がすぐでかくなる
大きいほうからやるほうがいい？
少なくとも小さいほうからやった時に、あんまりいい挙動をしているようには見えない
数字が大きいほうからのほうが、素数砂漠的に合計値が素数にhitする可能性はさがるのでは？
→　終わるのは速いけど55だと構成できないぞ…


候補の素数は5637個
選び方は5637C55

dpとその復元？

わからん、ギブアップ

解説後
ぐああああああ5の倍数狙いでmod計算かー
最初の5の倍数の発想は悪くなかった

"""