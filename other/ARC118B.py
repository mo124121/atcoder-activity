from heapq import heappop, heappush


K, N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [A[i] * M // N for i in range(K)]

h = []
for i in range(K):
    improve = abs(N * (B[i] + 1) - M * A[i]) - abs(N * B[i] - M * A[i])
    heappush(h, (improve, i))

for _ in range(M - sum(B)):
    imp, i = heappop(h)
    B[i] += 1

print(*B)


"""
数式変形して、ベースの数字を算出
余りを割り振ったほうがいいところに追加
"""
