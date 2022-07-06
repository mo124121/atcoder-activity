N, M = map(int, input().split())

A = [int(input()) for _ in range(M)]

seen = {}
ret = []
for a in reversed(A):
    if a not in seen:
        ret.append(a)
    seen[a] = True

for i in range(1, N + 1):
    if i not in seen:
        ret.append(i)

print(*ret, sep="\n")


"""
よく見る仕組みだけど考えたこともなかった
N<10**5

都度線形探索すると間に合わない、どうするか？

逆順にするのが楽かも
前に出てきたやつは無視
出てこなかったのは最後にappend


"""
