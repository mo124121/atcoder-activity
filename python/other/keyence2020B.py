N = int(input())

X = [0] * N
L = [0] * N
for i in range(N):
    X[i], L[i] = map(int, input().split())

T = [(X[i] + L[i], X[i] - L[i]) for i in range(N)]

T.sort()

prev = -(10**9) - 1

ret = 0
for r, l in T:
    if prev <= l:
        ret += 1
        prev = r

print(ret)


"""
貪欲にけしていくだけ…
に見えて、最初を残すか消すかで別れる

とするとやはりdpっぽい

N<10**5
X,L<10**9

言い換えるとタスク処理問題に近そう
X-Lから初めてX+Lに終わる仕事　どれだけ多く仕事ができるか？

とすると定石は終了順にソートして、順次埋めていくイメージ

"""
