#!/usr/bin/env python3
from bisect import bisect
import enum
from itertools import product


def gen_partial_sum(value_list, k, p):
    n = len(value_list)
    m = min(k, n)
    ret = [[] for _ in range(m + 1)]
    ret[0].append(0)

    for v in value_list:
        for i in range(m - 1, -1, -1):  # 逆向きにやると、自分が足した後に更に足しちゃうケースを回避できる
            for s in ret[i]:
                if s + v <= p:
                    ret[i + 1].append(s + v)
    return ret


def solve(N: int, K: int, P: int, A: "List[int]"):
    left = gen_partial_sum(A[: N // 2], K, P)
    right = gen_partial_sum(A[N // 2 :], K, P)

    ret = 0
    for x in range(K - len(right) + 1, len(left)):
        L = left[x]
        R = right[K - x]
        L.sort()
        R.sort()
        j = len(R) - 1
        for x, s in enumerate(L):
            while j >= 0 and s + R[j] > P:
                j -= 1
            if j < 0:
                break
            ret += j + 1

    print(ret)

    return


def main():
    N, K, P = map(int, input().split())
    A = list(map(int, input().split()))
    solve(N, K, P, A)


if __name__ == "__main__":
    main()


"""
考察
見るからにdpくさい
K,N<10**2 これをキーにしたい,一方でビット表現はできなさそう？2^40 -> 10**(3*4)
A,Pがごつい、ここをdpのキーにはできない
MODがない→無茶なパターン数は出てこない

深さ探索？いやビット表現の総数同様無理
でも枝切りなりキャッシュを使えば？
Xを追加した時のパターンはY<XなYを追加したパータン数と同じ
でもXにすることで増やせるパターンとかない？大丈夫？

価値をソートして小さいほうor大きいほうからやっていく
bisect使って放り込む？

いったんdpで書いて思考整理
→あきらめて解説読む

半分全列挙 N*2^(N/2)まで落とせる



"""
