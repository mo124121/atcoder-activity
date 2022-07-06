from bisect import bisect_left, bisect_right


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

B_right = [0] * N
B_right[0] = bisect_left(A, B[0])
for i in range(1, N):
    B_right[i] = bisect_left(A, B[i]) + B_right[i - 1]

ret = 0

for c in C:
    i = bisect_left(B, c)
    if i != 0:
        ret += B_right[i - 1]


print(ret)
"""
考察
N<10**5
O(NlogN)あたり

Cを走査しつつAとBを二分探索すればいいのでは？
それだとlen(C)*len(B)*log(len(A))で間に合わない

まとめてソートして右側ある個数を数える？3尺取り法？

別にCxBの回数せず、Blog(A)で二分探索して数えて覚えてから、
Clog(B)で結果だけ呼べばいいのでは？

解説後
真ん中を固定して上下側それぞれ二分探索でかければいい

"""
