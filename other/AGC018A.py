from heapq import heapify, heappop, heappush


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
if A[-1] < K:
    print("IMPOSSIBLE")
    exit()

B = [A[i + 1] - A[i] for i in range(N - 1)]

heapify(A)
for b in B:
    heappush(A, b)

elem = 10**10
prev = 0
while len(A):
    t = heappop(A)
    if prev != t:
        elem = min(elem, t - prev)
        prev = t

if K % elem == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

"""
とりあえず差をとっていくイメージ
繰り返してたどりつけなかったらおしまい

N<10**5
数が多いNlogNあたりがターゲット

できない条件
最大値よりでかい
倍数しかなくてたどりつけない

Anew=Aj-Ai
Anew2=Ak-Al
Anew3=Aj-Ai-Ak+Al

思い切ってKを引いてみたら？これは違いそう
むしろAmaxで引く？これは0から考えるのと同じ気がする

よくわからんけど通った


"""
