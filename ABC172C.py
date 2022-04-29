N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


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

"""
