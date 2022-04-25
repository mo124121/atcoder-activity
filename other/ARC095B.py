N = int(input())
A = list(map(int, input().split()))
A.sort()
ai = A[-1]
aj = -1
r = -1
for a in A[:-1]:
    if r < min(a, ai - a):
        aj = a
        r = min(a, ai - a)
print(ai, aj)

"""
二項係数を良く知っているか問題
とりあえずaiは一番大きい数字
ajは0とaiから最も離れる数字

nCr=nCn-r
max(min(r,ai-r))みたいな感じ？

"""
