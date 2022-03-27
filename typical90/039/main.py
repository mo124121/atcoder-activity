#!/usr/bin/env python3
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

size = [1] * 10 ** 6


def dfs(G, i, par=-1):
    for e in G[i]:
        if e == par:
            continue
        dfs(G, e, i)
        size[i] += size[e]


def solve(N: int, a: "List[int]", b: "List[int]"):
    G = defaultdict(list)
    for A, B in zip(a, b):
        G[A].append(B)
        G[B].append(A)

    dfs(G, 1)

    ret = 0
    for i in range(1, N + 1):
        ret += size[i] * (N - size[i])

    print(ret)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == "__main__":
    main()

"""
考察
dp!?

全パターンの最短経路の和
n=10**6 O(nlogn)まで行ける

木構造ゆえにループはない
自分の部分木はかならず自分を通る

再帰っぽい
木構造さえ作ってしまえばあとは番号関係ない
X:部分木内の距離の合算
Y:対部分木の根の距離の合算を保持
X+=親,およびマージされる他部分木との新規距離（X1_i+X2_j)

頂点Aに隣接する頂点数Mの部分木Bと頂点数Nの部分木Cが追加されたとすると、
X_A=Σ(Σ(Y_Bi+Y_Ci+2))=N*Y_B + M*Y_C 2*M*N
Y_Ai=[[Y_Bi+1],[Y_Ci+1],[0]]


想定解 主客転倒
ノードじゃなくてエッジ側で考える

"""
