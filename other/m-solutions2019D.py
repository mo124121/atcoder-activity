import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")

N = int(input())
from collections import Counter, defaultdict

G = defaultdict(list)
count = Counter()
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    count[a] += 1
    count[b] += 1
C = list(map(int, input().split()))

C.sort(reverse=True)
h = count.most_common()

M = sum(C) - max(C)
d = [0] * N
i = 0


def rec(node, par=0):
    global i
    d[node - 1] = C[i]
    i += 1
    for nxt in G[node]:
        if nxt != par:
            rec(nxt, node)


rec(h[0][0])

print(M)
print(*d)


"""
貪欲にやっていけばいいように見えるがどうか？
接続数が少ない方から小さい数字を割り当てる
接続数が多い方から大きい数字を割り当てる

一番大きい数は基本出てこない
ただ次に大きい数字を邪魔せずでてくることになる、連続で使いたい
自分が現れられるとこに置くか、次に大きいのが現れられる場所を増やすか
各場所でどちらがいいか考えればよい？

逆転はあるか？
たぶんない

接続数が大きい方から大きい数字を割り当てるでFA　実装する


これ、もっと言うと最大値以外はすべて出てくるし、
総計-最大値が答えでは？
あとは適当に構成すれば勝ち
最小値が端っこにくれば良い
嘘だわ、大きい順に埋める必要はある、じゃないと死ぬ

接続数が多い順ではなく、接続数が一番大きいところを根として幅なり深さなり探索して
先に出てきたほうから振っていく
"""
