from heapq import heapify, heappop, heappush


N, L = map(int, input().split())
A = list(map(int, input().split()))
ret = 0
heapify(A)
L -= sum(A)
if L > 0:
    heappush(A, L)
while len(A) > 1:
    p1 = heappop(A)
    p2 = heappop(A)
    pn = p1 + p2
    ret += pn
    heappush(A, pn)
print(ret)
"""
あり本で見たやつやわ
kを分割するやつのにコストがかかる
逆heapで行けるはず
普通にheapと思ったらWAやったわ


"""
