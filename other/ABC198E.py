from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
N = int(input())
C = list(map(int, input().split()))

G = defaultdict(list)
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

count = defaultdict(int)
ret = []


def rec(node, par=0):
    count[C[node]] += 1
    if count[C[node]] == 1:
        ret.append(node + 1)
    for child in G[node]:
        if child != par:
            rec(child, node)
    count[C[node]] -= 1


rec(0)
ret.sort()
print(*ret, sep="\n")


"""
グラフ　木
探索しつつ、辞書で色ごとの個数をカウントする
辞書の追加・削除が走るので、
再帰のほうが相性よさそう？
"""
