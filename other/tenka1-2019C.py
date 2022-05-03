N = int(input())
S = input()

w = [0] * (N + 1)
b = [0] * (N + 1)

for i in range(N):
    w[i + 1] = w[i] + int(S[i] == "#")

for i in range(N, 0, -1):
    b[i - 1] = b[i] + int(S[i - 1] == ".")

ret = 10**6
for i in range(N + 1):
    ret = min(ret, w[i] + b[i])

print(ret)

"""
.....######
みたいな状況にしたい
左から見て、i番目までを.で埋めるコスト
右から見て、j番目までを#で埋めるコスト
それらが最小になる場面がベスト

自力AC
BIT使うのもいいのかも
"""
