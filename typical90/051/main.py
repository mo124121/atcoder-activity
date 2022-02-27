#!/usr/bin/env python3
from bisect import bisect
from itertools import product



def gen_partial_sum(value_list):
    n = len(value_list)
    ret = [[] for _ in range(n + 1)]
    st=[(-1,0,0)]

    while len(st):
        i,s,c=st.pop()
        if i+1<n:
            st.append((i+1,s+value_list[i+1],c+1))
            st.append((i+1,s,c))
        else:
            ret[c].append(s)

    return ret


def solve(N: int, K: int, P: int, A: "List[int]"):
    B = gen_partial_sum(A[: N // 2])
    C = gen_partial_sum(A[N // 2 :])

    ret = 0
    for i in range(max(0,K-len(B)),min(len(C),K+1)):
        B[K - i].sort()
        for p in C[i]:
            j = bisect(B[K - i], P - p)
            ret += j

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
