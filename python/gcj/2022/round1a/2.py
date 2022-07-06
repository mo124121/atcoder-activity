T = int(input())
A = []
for i in range(30):
    A.append(1 << i)
for i in range(29):
    A.append(3 << i)
for i in range(28):
    A.append(5 << i)
for i in range(13):
    A.append(10 * 9 - 1 << i)
sum_A = sum(A)

for t in range(T):
    N = int(input())
    print(*A, flush=True)
    B = list(map(int, input().split()))
    tot = sum_A + sum(B)
    target = tot // 2
    cur = 0
    AB = A[:] + B
    AB.sort(reverse=True)
    ret = []
    for b in AB:
        if cur + b < target:
            cur += b
            ret.append(b)
        else:
            break
    diff = target - cur
    for i in range(30):
        q = 1 << i
        if diff >> i & 1:
            ret.append(q)
    print(*ret, flush=True)


"""
考察
インタラクティブとか知らんがね

dpっぽくはあるよね
何個か使ってとれる値
ただ値の範囲が広いのでそうもいかない
値の範囲 <10^9

そのままやると多項式時間では終わらない
けど半分こちらで決めたらそうでもないってどういうこと？
合計したら偶数になる->奇数になったら解けなくなる

とすると問題設定的に活用できそうなものがない、どうする？

まず全列挙を考えてみる
全パターン
2^(2*100)

先に決める、というののしんどさ

bitで考えてみるとか？

X:全体の合計
とすれば
X//2がターゲット

値が同じ=bitが一致する
Xの最高桁数以外が一致する

N=100が怪しい
どんな値にも対応できるのを提案する
2^30

大きいほうから固めたいが、さて

たぶんパリティ的な考え方


"""
