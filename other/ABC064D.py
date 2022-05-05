from collections import deque


N = int(input())
S = input()
l_count = 0
r_count = 0
tmp = 0
for c in S:
    if c == ")":
        if tmp == 0:
            l_count += 1
        else:
            tmp -= 1
    else:
        tmp += 1
tmp = 0
for c in S[::-1]:
    if c == "(":
        if tmp == 0:
            r_count += 1
        else:
            tmp -= 1
    else:
        tmp += 1

print("(" * l_count + S + ")" * r_count)

"""
見るからにstack
dequeで両側から削っていく？
取り出したやつは左と右でストックしてあとでがっちゃんこする

がっちゃんこする、というのがsmartでない
dequeに番兵をいれておき、補う操作をした後で、取り出すとか？

中途半端に触ると沼にはまりそう
相性がいいのはstack
あるいは違う法則性を見つけるか

基本的にstackで触りつつ、状況に応じてdequeに追加していく形

元の配列
状態を保存するstack
結果を保存するdeque

あんまり複雑なことは考えなくてよくて、
左から見て行って足りないときにすぐ左で補って、最後多いときに右を補えばいいのでは？

辞書順最小…
となるとなるべく(は左に置きたいし、)は右に置きたい

左から見てオープンな)の数を左に足す
右から見てオープンな(の数を右に足す

"""
