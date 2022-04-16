N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [0] * (1 + M)
B[M] = C[N + M] // A[N]

for m in range(M - 1, -1, -1):
    for n in range(max(0, N - (M - m)), N):
        B[m] -= A[n] * B[m + (N - n)]
    B[m] = (C[m + N] + B[m]) // A[N]

print(*B)

"""
非初見、数式計算必要なやつ
添え字がバグる

大きいほうからおろしたい
M-1, M-2...
Aはどうなるか？
M-1:M-i=M-M+1=1回 N-1*M-0 
M-2:M-i=M-M+2=2回 N-2*M-0,N-1*M-1 


終わった後整理
なるべく直観的に添え字を使うようにする
添え字がどう動くか？


"""
