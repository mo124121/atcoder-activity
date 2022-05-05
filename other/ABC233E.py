from collections import deque


X = list(map(int, list(input())))
ret = deque()
S = sum(X)

tmp = 0
for x in reversed(X):
    tmp += S
    ret.appendleft(tmp % 10)
    tmp //= 10
    S -= x
if tmp != 0:
    ret.appendleft(tmp)
print(*ret, sep="")

"""
全体のsumをとりつつ、桁上がりとsumから引いたやつを足していく
"""
