from itertools import product


N = int(input())
S = list(map(lambda x: int(x == "x"), list(input())))
S = S + [S[0], S[1]]
m = "SW"
for (first, second) in product(("S", "W"), repeat=2):
    ret = ["N"] * len(S)
    ret[0] = first
    ret[1] = second
    for i in range(1, N + 1):
        ret[i + 1] = m[(S[i] + int(ret[i - 1] == "W") + int(ret[i] == "W")) % 2]
    if ret[:2] == ret[-2:]:
        print(*ret[:-2], sep="")
        exit()
print(-1)
