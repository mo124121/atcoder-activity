N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))


def get_zero_indices(U):
    ret = []
    for i, c in enumerate(U):
        if c == 0:
            ret.append(i)
    return ret


S_zeros = get_zero_indices(S)
T_zeros = get_zero_indices(T)
if len(S_zeros) != len(T_zeros):
    print(-1)
    exit()

ret = 0
for s, t in zip(S_zeros, T_zeros):
    if s != t:
        ret += 1
print(ret)

"""
00001->10000
11110->01111

操作で増減はできない->1の数が合わないのは-1

貪欲にやっていくのがいい？　が間に合わない
N<5*10**5

とりあえず圧縮した表を持っておいて、
順次消化していくとか
いずれにせよ1個ずつしか動かせない
テーブルを活用して埋めていく

間違ってますねはい

移動量の最大化を狙う
うまくやると1度できる操作が2つに分割されてしまうイメージ

発想の問題な気がする解説見る
あー問題よみまちがえてるーーーー
ただそれでも間違っている

0の位置に着目する->数が少ないほうに着目する典型
0の位置とそのズレに着目する
そのずれ数を最小値として出力


"""
