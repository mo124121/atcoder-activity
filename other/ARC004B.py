N = int(input())
D = [int(input()) for _ in range(N)]
D_max = max(D)
ret_max = sum(D)
ret_min = max(0, D_max - (ret_max - D_max))
print(ret_max, ret_min, sep="\n")

"""
最大値は楽勝に見える
問題は最小値

N<500
N**3<125*10**6<2*10**8
一致できるかはまあdpっぽい感じでやったら行けそう

とりうる範囲というのを示すイメージ？

結局一番長いものをどこまで消しこめるか、という話な気がする
そこが届くならあとはどうとでもなりそう

"""
