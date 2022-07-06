from heapq import heapify, heappop, heappush


K, T = map(int, input().split())
A = list(map(int, input().split()))
big = max(A)

ret = max(0, big - (K - big + 1))

print(ret)


"""
ヒープで管理して、数が多いものから食べていくイメージ

一番多いやつからほかの合計を引いたやつでいいのでは？

"""
