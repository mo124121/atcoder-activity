N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
prev_ng = -1
prev_y = -1
prev_x = -1
ret = 0
for i in range(N):
    if A[i] == X:
        prev_x = i
    if A[i] == Y:
        prev_y = i

    if A[i] > X or A[i] < Y:
        prev_ng = i
        prev_y = i
        prev_x = i

    ret += min(prev_x, prev_y) - prev_ng


print(ret)

"""
考察

N<10**5
O(NlogN)

Xを含む範囲
Xより大きい数を含まない範囲
Yを含む範囲
Yより小さい数を含まない範囲

segtreeは強力だが使いどころが重要

NGな数を含む所で分割して考えていい、絶対にまたぐことはない

という訳でY<=A<=Xの数列を考える

Xの右端xYの左端

dp的に考える
数列を増やしたときに伸びる数は何個か？
X!=Ai!=Yの時 ベースとなるパターン数分たされる
X==Aiの時 最後のYが出てくるところがベースになる
Y==Aiの時 最後のＸが手てくるところがベースになる

そもそも単調増加的ではないが？

"""
