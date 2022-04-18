from collections import defaultdict


N = int(input())
V = list(map(int, input().split()))

size = [0] * 2
count = [defaultdict(int) for _ in range(2)]

for i, v in enumerate(V):
    count[i % 2][v] += 1
    size[i % 2] += 1

c_2 = [[(v, i) for i, v in count[j].items()] for j in range(2)]
c_2[0].sort(reverse=True)
c_2[1].sort(reverse=True)

if c_2[0][0][1] != c_2[1][0][1]:
    print(N - c_2[0][0][0] - c_2[1][0][0])
else:
    if len(c_2[0]) > 1:
        c_o_sub = c_2[0][1][0]
    else:
        c_o_sub = 0
    if len(c_2[1]) > 1:
        c_e_sub = c_2[1][1][0]
    else:
        c_e_sub = 0
    print(N - max(c_o_sub + c_2[1][0][0], c_2[0][0][0] + c_e_sub))

"""
奇数位置・偶数位置に出てくる数字それぞれについて、個数をカウント
例外を除き、それぞれ一番大きいやつ以外の合計値が必要な操作数になる

問題は一番大きいのが偶数位置・奇数位置で同じな場合
コストが増えないほうが優先になる
それぞれ2番目に入れ替えた場合での悪化が少ないほうにする


"""
