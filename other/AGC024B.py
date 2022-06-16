N = int(input())
P = [int(input()) for _ in range(N)]

ls = dict()

for p in P:
    if p in ls:
        ls[p + 1] = ls[p] + 1
    else:
        ls[p + 1] = 1

print(N - max(ls.values()))


"""
自明な上界がありそうな問題
個数-転倒がない個数

見立てがあまそう

全体の個数-１ずつ増える部分列の最大長

dpっぽい

辞書でうまくコントロールするイメージ

"""
