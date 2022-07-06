from collections import deque


N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

A.sort(reverse=True)

if N % 2 == 0:
    ret = 0
    for i in range(N // 2 - 1):
        ret += A[i] * 2
    ret += A[N // 2 - 1] - A[N // 2]
    for i in range(N // 2 + 1, N):
        ret -= A[i] * 2
else:
    ret1 = 0
    for i in range(N // 2 - 1):
        ret1 += A[i] * 2
    ret1 += A[N // 2 - 1] + A[N // 2]
    for i in range(N // 2 + 1, N):
        ret1 -= A[i] * 2

    ret2 = 0
    for i in range(N // 2):
        ret2 += A[i] * 2
    ret2 -= A[N // 2] + A[N // 2 + 1]
    for i in range(N // 2 + 2, N):
        ret2 -= A[i] * 2
    ret = max(ret1, ret2)

print(ret)

"""
考察

N<10**5
O(NlogN)
ソート使える

ソートして適当に遠いほうから選んだらでかくならない？

1 2 8 9
1 7 7 9

そんなことはなかった

全接続のグラフの最大コスト問題？ V^2になるので間に合わなそう

基本的に最大と最小をから交互にピックすればいいが、
一番小さいのは真ん中に置きたい、どういうことか？

むしろ価値が低いやつが端にくるイメージ？
dequeで交互に入れて最後にlist化してスコア計算かも

解説後
それぞれの足し引きの回数に帰着される




"""
