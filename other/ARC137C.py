N = int(input())
A = list(map(int, input().split()))

if A[-1] - A[-2] > 1:
    print("Alice")
    exit()

if (A[N - 1] - (N - 1)) % 2 == 1:
    print("Alice")
else:
    print("Bob")


"""
要は空き手数がなくなったら負け、的な
空き手数=最大値-個数

基本場を作れるAliceが勝ちそう？
要は相手のを見て終わりを修正していくイメージ

選択肢をつぶせる盤面が何か所あるか？

必勝法がわからん
ただ、「最適手」と言われるものがあるのであれば、
お互いに勝ち方が必ずあり、お互いのパターンでは発散しないはず
負ける側は選択によらず負ける、的な感じのはず（じゃないと勝ち筋がある=そちらを選べばよい）
局面での趨勢はなく、ある盤面で既に勝ち負けが決している状態

s 2 4
a 2 3
b 1 2
a 0 1
b x

s 2 4
a 0 2
b 0 1 
a x

s 0 1 2
a x

s 2 5
a 2 3
b x

s 2 5
a 2 4
a x

s 2 4 6
a 2 4 5

s 3 4
a 2 3
b 1 2
a 0 1
b x

s 1 3 5
a 1 3 4
b 0 1 3
c 0 1 2
"""
