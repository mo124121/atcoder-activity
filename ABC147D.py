N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
ret = 0
for k in range(61):
    x = 0
    for j in range(1, N):
        x += int((A[j - 1] >> k) & 1)
        if int((A[j] >> k) & 1) == 0:
            y = x
        else:
            y = j - x
        ret += y * 2**k
        ret %= MOD

print(ret)


"""
XORの性質を使うべき
bitで分解してjまでに立ってるbit数を数えるx
jのbitが立ってるかどうかで上記x or j-1-xで産出する

AC

解説
1と0の組み合わせの数なので、それぞれの個数をカウントして積をとった個数
超賢い
"""
