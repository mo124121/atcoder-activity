#!/usr/bin/env python3
import sys


class Grundy:
    def __init__(self) -> None:
        W = 50
        B = W * (W + 1) // 2
        memo = [[0] * (B + W + 1) for _ in range(W + 1)]

        for w in range(W + 1):
            for b in range(B + 1):
                mex = [0] * (B + W + 1)
                if w >= 1:
                    mex[memo[w - 1][w + b]] = 1
                if b >= 2:
                    for k in range(1, b // 2 + 1):
                        mex[memo[w][b - k]] = 1
                for k in range(B + W + 1):
                    if mex[k] == 0:
                        memo[w][b] = k
                        break
        self.memo = memo

    def count(self, w, b):
        return self.memo[w][b]


def solve(N: int, W: "List[int]", B: "List[int]"):
    count = 0
    grundy = Grundy()

    for w, b in zip(W, B):
        count ^= grundy.count(w, b)

    if count == 0:
        print("Second")
    else:
        print("First")

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

入力例2が示唆に富んでいる
同じ形状の山があったら後手は相手と同じ操作をすればいい
同じ山ないしは同じ山とみなせる形状をつくれるんだったら、
偶数個の同じ山はないものと思っていい


とすればあとは白による挙動を考える
どう場合分けする？
青は選択肢がいくつかあるのに対して、白は一つの操作しか許容していない

S 2 3, 2 4
F 2 1, 2 2, 1 5, 1 6, 1 7, 1 8
S 1 3, 1 4, 2 0(初期のみ)
F 1 2
S 1 1, 0 3, 0 4
F 0 2, 1 0
S 0 1, 0 0

ちょっと複雑　wが1の時は挙動がちょっと変
ただ、要は(w%2+(b手番偶奇)) xN みたいな感じ
実装に移る


解説後
こういうゲームをGrundy数と言われるもので考えることが分かった


"""