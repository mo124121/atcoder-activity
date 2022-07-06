from collections import defaultdict


T = int(input())
ret = []
for t in range(T):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    G = defaultdict(list)
    for i, p in enumerate(P):
        G[p].append(i + 1)


print(*ret, sep="\n")


"""
考察
N<10**6

分岐がないのは黙ってmaxとったらいい
連続しているのはmaxで圧縮していい
手動でトリガーする側から考えてもいいが、abyss側から考える方が楽そう
"""
