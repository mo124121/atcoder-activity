from itertools import product


N = int(input())

for pat in product([*"abc"], repeat=N):
    print(*pat, sep="")
