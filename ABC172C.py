from bisect import bisect_right


N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(N - 1):
    A[i + 1] += A[i]
for i in range(M - 1):
    B[i + 1] += B[i]

ret = bisect_right(B, K)
for i, a in enumerate(A):
    if a <= K:
        ret = max(ret, i + 1 + bisect_right(B, K - a))
    else:
        break

print(ret)

"""
N,M<=200000
見るからにDPの問題設定
A,Bのとる値が大きいので、
読んだ冊数がindex
dp[i]:i冊読む時の最短時間
なんか違う気がする

そもそもAとBの操作は独立
両方累積和を取ったうえで、
片方を動かしながら、反対側でとれる個数を二分探索

2WA
コーナーケースくさい

a<K -> a<=Kに変えたらAC
a=Kならbがとれなくてもとれるから

AC
解説後
尺取り法でも行ける

"""
