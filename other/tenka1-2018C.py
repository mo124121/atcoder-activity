from collections import deque


N = int(input())
A = [0] * N
for i in range(N):
    A[i] = int(input())

A.sort()

dq = deque()
l = 0
r = N - 1
flag = True
while l < r:
    if flag:
        dq.appendleft(A[l])
        l += 1
    else:
        dq.append(A[r])
        r -= 1
    flag ^= True
pre = dq.popleft()
ret = 0
while len(dq):
    post = dq.popleft()
    ret += abs(pre - post)
    print(pre, post, ret)
    pre = post


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
