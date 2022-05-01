N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 10**9 + 7

"""
時間はないが考察を頑張る
N,M<1000
N*M<10*6

ある行・列には特定の数字を消化する必要が出てくる
ある行にはその数字はかならずあるし、それ以外の数字はその数字より小さい


"""
