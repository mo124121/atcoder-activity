N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append((a, i))
A.sort()
ret = 0
for i in range(0, N, 2):
    if A[i][1] % 2 == 1:
        ret += 1
print(ret)


"""
奇数番目と偶数番目は好きにソートできる

すごい雑にやると、全体をソートして、
奇数番目に来るべきものが偶数番目にきた場合にスワップが必要なのでその回数
あってたわ

"""
