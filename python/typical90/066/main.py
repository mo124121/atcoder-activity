#!/usr/bin/env python3
import sys


def solve(N: int, L: "List[int]", R: "List[int]"):
    ret = 0
    for i in range(1, N):
        for j in range(i):
            count = 0
            for k in range(L[j], R[j] + 1):
                for l in range(L[i], R[i] + 1):
                    if l < k:
                        count += 1
            ret += count / ((R[j] - L[j] + 1) * (R[i] - L[i] + 1))
    print(ret)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, L, R)


if __name__ == "__main__":
    main()


"""
考察
期待値？モンテカルロ？（小声）

N<100
L<=R<100
制約は小さめ->N^3 あたりを狙いたくなる

これもdpくさい
要素が増えるごとの期待値を計算していくイメージ？

そもそも転倒数とは何か？
LISの降順,LDS　違う　最長である必要はない
全組み合わせの個数なら、過去のとる値の範囲×今回採用する値の範囲で適当に計算したらええんちゃうの？



"""