from collections import deque


N = int(input())
S = input()

L = [0] * (N + 1)
for i, c in enumerate(S):
    L[i + 1] = L[i]
    if c == "#":
        L[i + 1] += 1

R = [0] * (N + 1)
for i in reversed(range(N)):
    R[i] = R[i + 1]
    if S[i] == ".":
        R[i] += 1

ret = 10**10
for i in range(N + 1):
    ret = min(ret, R[i] + L[i])

print(ret)


"""
....#####
#..##..##

端から見ていって、黒を変えるのと、
白を変えるのがどっちがコストか考える
ランレングス圧縮するといい

まて、左から白埋めしていくコスト
右から黒埋めしていくコストをそれぞれ求める
各点でのコストトータルを計算して最小を探す

"""
