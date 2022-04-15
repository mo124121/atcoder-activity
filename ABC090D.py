N, K = map(int, input().split())

ret = 0
for b in range(K + 1, N + 1):
    ret += max(0, b - K) * (N // b)
    if K != 0:
        ret += max(0, N % b - K + 1)
    else:
        ret += max(0, N % b)
print(ret)

"""
考察

連続してあまり考えるやつ　なんか嫌われている気がする

a mod b > K

bを上げながら対応する個数を数え上げる
対応する個数は
N//b個*K個以上の数
コーナーケース的な発想が難しい

解説後
K==0がコーナーケース
割り切れる範囲の最大値のところと、
最後の端数のスタートのところで2重に数えてしまう

"""
