H, W, A, B = map(int, input().split())

line = A * "0" + (W - A) * "1"
line_neg = A * "1" + (W - A) * "0"

for i in range(H):
    if i < B:
        print(line)
    else:
        print(line_neg)

"""
小さいほうがAとかB
なんというか、偏りが必要
W//2が制約なし、みたいな感じ

とりあえずA=0でB>0だと無理
なんかうまく散らしたらできそうなんだよなあ
いや、真っ黒と真っ白組み合わせたらよろし

AとBが割り切れる関係が必要に見える

あーでも反転できるのか

割と自由度高いのでNoがなさそう、あるのかな

AC
"""
