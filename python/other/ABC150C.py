from itertools import permutations


N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

Pseq = list(permutations(list(range(1, N + 1))))
print(abs(Pseq.index(P) - Pseq.index(Q)))
