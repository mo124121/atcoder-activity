from collections import defaultdict
from itertools import permutations


N = int(input())
S = input()

ABC = "ABC"
num_pos = [defaultdict(list) for _ in range(3)]
for j in range(N):
    for k in range(3):
        pos = k * N + j
        num_pos[k][S[pos]].append(pos)

ret = [0] * (3 * N)
for i, c in enumerate(permutations(ABC)):
    while len(num_pos[0][c[0]]) and len(num_pos[1][c[1]]) and len(num_pos[2][c[2]]):
        for k in range(3):
            ret[num_pos[k][c[k]].pop()] = i + 1

print(*ret, sep="")

"""
解説みてもうた
発想が無理
と思ったらそうでもない

ホールの定理

"""
