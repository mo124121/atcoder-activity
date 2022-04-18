from heapq import heappop, heappush


N, M = map(int, input().split())
A = list(map(int, input().split()))

h = []

for a in A:
    heappush(h, -a)

for _ in range(M):
    a = -heappop(h)
    a //= 2
    heappush(h, -a)

print(-sum(h))


"""
N,M<10**5
N**2は厳しい

チケットを使うほど半額にできる
操作後の高いものから使いたい
ヒープで半分にしていって最後に合算したらよい

"""
