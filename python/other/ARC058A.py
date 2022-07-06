N, K = map(int, input().split())
D = list(map(int, input().split()))
ng = set()
for d in D:
    ng.add(str(d))

for i in range(N, 10**6):
    digits = str(i)
    flag = True
    for d in digits:
        if d in ng:
            flag = False
            break
    if flag:
        print(i)
        exit()

"""
二分探索しちゃう？

N<10**4
N**2あたりは行ける

上から決めていくイメージ？再帰っぽい
Nd:Nのdigit

Ndより小さい数字しかない場合
Ndと同じ数字がある場合
Ndより大きい数字がある場合

場合分けがしこたまめんどくさい
もうちょっと賢い方法はないか？

1WA,3RE/10
4WA/10
3WA/10

これごり押しでも良くない？

はい全探索でAC

"""
