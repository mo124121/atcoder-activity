from bisect import bisect_left


N, K = map(int, input().split())
D = list(map(int, input().split()))
D_inv = []
for i in range(10):
    if i not in D:
        D_inv.append(i)
M = len(D_inv)


def rec(X):
    top = int(X[0])
    if len(X) == 1:
        i = bisect_left(D_inv, top)
        if i == M:
            return True, [D_inv[0]]
        else:
            return False, [D_inv[i]]

    flag, ret = rec(X[1:])

    if flag:
        i = bisect_left(D_inv, top + 1)
    else:
        i = bisect_left(D_inv, top)

    if i == M:
        return True, [D_inv[0]] * len(X)
    else:
        if D_inv[i] == top:
            return False, [D_inv[i]] + ret
        else:
            return False, [D_inv[i]] + [D_inv[0]] * (len(X) - 1)


_, r = rec(str(N))
print(*r, sep="")


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


"""
