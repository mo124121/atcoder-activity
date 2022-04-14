#!/usr/bin/env python3
import sys


def solve(N: int, W: "List[int]", B: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W, B)


if __name__ == "__main__":
    main()


"""
考察
命名-手番分析

考えるべき要素 偶数番と奇数番

片方は状況をコントロールできるけど、片方は何をしても吸収されるイメージ

とれる状態遷移を考える
操作可能な山で
　wで一つ減らす& w個bを増やす
　bで1~floor(2/b)のどれか減らす
山を跨いでの操作はない

規模分析
N<10^5
Wi,Bi<50

WxBの全ての最適推移を計算し、偶奇が決められる
それをN回合計した後の結果を考える、とか？


となると最適なとり方は何か？一つの山を考える

まず青

F 0 5, 0 6, 0,7 0 8
S 0 3, 0 4 
F 0 2　★　この手番にできる人になれるか？
S 0 1

こう見ていくと青は個数見たら決まりそう　後の手番で前の操作を吸収できる

wがどう作用するか？
相手の操作をキャンセルするイメージ？
でも数字次第　集約はできそう

"""
