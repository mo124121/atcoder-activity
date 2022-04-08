#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()


"""
考察
N<200　小さい N^3までは行けそう

全部の消していくパターンを考えると N!

単調増加を仮定すると、
0 : 0 5 15 20 21 30
1 : 0 5 15 30  
16: 0 5

0 : 0 5 15 20 21 30
9 : 0 5 15 20
14: 0 5

端の方から削除していく方がいい感じ
そういう意味で、「飛びてる数値」を起点に消していくのがよい？
出っ張ってるところをそこで消してもらえると後のコスト低減に繋がる
じゃあどうやって飛び出ているを選ぶのか？

なんとなく状態遷移っぽくて、
消す順番性をmin(cost)で消していくとか？




"""
