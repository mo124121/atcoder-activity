from collections import deque


N, R = map(int, input().split())
S = list(input())
prev = 0
ret = 0
r = 0
shot = 0
while "." in S:
    while len(S) > 0 and "o" == S[-1]:
        S.pop()
    r = max(r, len(S) - R)
    S = S[: -min(R, len(S))]
    shot += 1
ret = r + shot

print(ret)

"""
少し条件分岐が複雑
面倒だからごり押しする

あー書いてくと面倒

後ろからやるのがいいか？

AC
解説後
右端を見つけた後で、左から貪欲にやればよろしい

"""
