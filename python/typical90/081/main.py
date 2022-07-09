#!/usr/bin/env python3
import sys

MAX = 5000


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    MAX = max(max(A), max(B))

    dp = [[0] * (MAX + 2) for _ in range(MAX + 2)]

    for i in range(N):
        a_min = A[i]
        a_max = min(A[i] + K, MAX) + 1
        b_min = B[i]
        b_max = min(B[i] + K, MAX) + 1

        dp[a_min][b_min] += 1
        dp[a_min][b_max] -= 1
        dp[a_max][b_min] -= 1
        dp[a_max][b_max] += 1

    ret = 0
    for i in range(MAX + 2):
        for j in range(MAX + 1):
            dp[i][j + 1] += dp[i][j]
    for j in range(MAX + 2):
        for i in range(MAX + 1):
            dp[i + 1][j] += dp[i][j]
            ret = max(ret, dp[i][j])

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
    K = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, K, A, B)


if __name__ == "__main__":
    main()


"""
考察
N<2*10^5
K<5000
N^2はきつい、KNあたりも微妙か

ソートして尺取り法っぽくはある、ただ2次元だとわからん
1次元なら尺取りで解ける
身長で尺取りして、その範囲でソートして尺取りするとどうなる？
ソートO(NlogN) + 身長尺取りO(N) * (ソートO(NlogN)*体重尺取りO(N)）=O(N^2logN)

multiset出てきそう…

発想を変える
x:身長、y:体重で各人をプロットした時、K x Kの箱を置くときに一番たくさん入る置き方、みたいな問題
とすると、ある人がx,yとすると、[x-K,x+K],[y-K,y+K]の範囲はその人がチームに入れる
つまり全員の範囲を合算して、一番大きいのを見つければ良い。　O(N+K^2)
すなわち2次元いもす、勝った。実装を忘れたこと以外は…

いもすの考え方が違いそう、上だと幅が広すぎる
[x,x+K][y,y+K]にしようか
sample AC, test WA


"""