from collections import Counter


A = input()

count = Counter(A)
n = len(A)
ret = n * (n - 1) // 2
for v in count.values():
    ret -= v * (v - 1) // 2
print(ret + 1)

"""
反転するところが回文だったらNG
ローリングハッシュ使えばO(N**2)は行けそう


ちょっと違いそう

ある位置に着目して、同じなら左右に広げるイメージ？
それでもN**2かかりそう

わからん
解説読む

この証明と書き換えを自信もってやるの結構厳しい…
と思ったけど、無駄に難しく考えていただけだった気がする

数字が同じペアはなかったものとして考えていいよね、という話


"""
