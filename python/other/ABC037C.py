N, K = map(int, input().split())
A = list(map(int, input().split()))

r = sum(A[:K])
ret = r
for i in range(K, N):
    r += A[i] - A[i - K]
    ret += r

print(ret)
"""
考察
各項が出てくる個数を考えたらよい、がちょっとややこしい？
場合分けが必要

それをするぐらいなら愚直にずらすほうが賢くない？

AC後解説
各位置までのsumを先に計算しとくのも確かにあり
あとBITでもいいね

"""
